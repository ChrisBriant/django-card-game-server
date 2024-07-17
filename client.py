from autobahn.asyncio.websocket import WebSocketClientFactory, WebSocketClientProtocol
import asyncio

class MyClientProtocol(WebSocketClientProtocol):
    async def onOpen(self):
        #self.sendMessage(u"Hello, world!".encode('utf8'))
        self.sendMessage(u"""{
          "token" : "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIwOTM1ODkxLCJpYXQiOjE3MjA5MzU1OTEsImp0aSI6IjdkNDI3MzU4YjYwNjQyYTI4MmQ1ODEyNzZhNGIxNGFiIiwidXNlcl9pZCI6Mn0.tJNhxXf5WIraoTZ_7bzvC6EFk7J6LqNUDFnXGKC8FKo",
          "message": "Hello, server!"
        }""".encode('utf8'))

    async def onMessage(self, payload, isBinary):
        print("Received message: {}".format(payload.decode('utf8')))

if __name__ == '__main__':
    factory = WebSocketClientFactory("ws://127.0.0.1:8000/ws/cards-consumer/?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIwOTg4NjQxLCJpYXQiOjE3MjA5NzQyNDEsImp0aSI6ImQyOTIwMTQxMzgyZTRhNWJhNWRjZTM3MWM3MDA3OWQxIiwidXNlcl9pZCI6Mn0.AE1o-w8dwXBw1rc_BIOWhWftZ1o5t_-QRa03611EQuw")
    factory.protocol = MyClientProtocol

    loop = asyncio.get_event_loop()
    coro = loop.create_connection(factory, '127.0.0.1', 8000)
    loop.run_until_complete(coro)
    loop.run_forever()