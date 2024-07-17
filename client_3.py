import asyncio
from autobahn.asyncio.websocket import WebSocketClientFactory, WebSocketClientProtocol, ConnectionRequest
from autobahn.websocket.protocol import WebSocketProtocol

class MyClientProtocol(WebSocketClientProtocol):
    async def onConnect(self, response):
        print("Connected to server")

    async def onOpen(self):
        print("WebSocket connection open.")

    async def onMessage(self, payload, isBinary):
        print(f"Received message: {payload.decode('utf8') if not isBinary else 'Binary message'}")

    async def onClose(self, wasClean, code, reason):
        print(f"WebSocket connection closed: {reason}")

class MyClientFactory(WebSocketClientFactory):
    def __init__(self, url, token):
        super().__init__(url)
        self.token = token

    def buildProtocol(self, addr):
        protocol = super().buildProtocol(addr)
        protocol.factory = self
        return protocol

    def createHeaders(self):
        headers = [
            (b'Authorization', f'Bearer {self.token}'.encode('utf-8'))
        ]
        return headers

    def _createRequest(self):
        request = ConnectionRequest()
        request.headers.update(self.createHeaders())
        return request

if __name__ == '__main__':
    token = "your_jwt_token_here"
    factory = MyClientFactory("ws://127.0.0.1:8000/ws/cards-consumer/", token)
    factory.protocol = MyClientProtocol

    loop = asyncio.get_event_loop()
    coro = loop.create_connection(factory, '127.0.0.1', 8000)
    loop.run_until_complete(coro)
    loop.run_forever()