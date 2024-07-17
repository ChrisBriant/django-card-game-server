import asyncio
from autobahn.asyncio.websocket import WebSocketClientFactory, WebSocketClientProtocol

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

    def getConnectionHeaders(self):
        headers = super().getConnectionHeaders()
        headers["Authorization"] = f"Bearer {self.token}"
        return headers

if __name__ == '__main__':
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIwOTg4NjQxLCJpYXQiOjE3MjA5NzQyNDEsImp0aSI6ImQyOTIwMTQxMzgyZTRhNWJhNWRjZTM3MWM3MDA3OWQxIiwidXNlcl9pZCI6Mn0.AE1o-w8dwXBw1rc_BIOWhWftZ1o5t_-QRa03611EQuw"
    factory = MyClientFactory("ws://127.0.0.1:8000/ws/cards-consumer/", token)
    factory.protocol = MyClientProtocol

    loop = asyncio.get_event_loop()
    coro = loop.create_connection(factory, '127.0.0.1', 8000)
    loop.run_until_complete(coro)
    loop.run_forever()