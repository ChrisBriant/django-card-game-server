import json
from channels.generic.websocket import AsyncWebsocketConsumer


class CardsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('SOMEONE HAS MADE A BAD SMELL')
        await self.accept()

    # async def connect(self):
    #     print('SOMEONE HAS CONNECTED')
    #     self.room_name = 'test_room'
    #     self.room_group_name = 'test_group'

    #     await self.channel_layer.group_add(
    #         self.room_group_name,
    #         self.channel_name
    #     )

    #     await self.accept()

    # async def connect(self):
    #     print('I WILL TRY')
    #     from rest_framework_simplejwt.exceptions import InvalidToken
    #     from api.utils import get_user_id_from_jwt
    #     from django.contrib.auth import get_user_model
    #     from asgiref.sync import sync_to_async

    #     try:
    #         User = get_user_model()
    #         token = self.scope['query_string'].decode().split('=')[1]
    #         headers = dict(self.scope['headers'])
    #         print("HEADERS", headers)
    #         auth_header = headers.get(b'sec-websocket-protocol')

    #         if not auth_header:
    #             print("NO AUTH HEADER")
    #             await self.close(reason='Authorization header missing')
    #             return

    #         # Extract token from the header
    #         token = auth_header.decode().split(' ')[1]
    #         print("TOKEN EXTRACTED FROM THE HEADER", token)
    #         user_id = get_user_id_from_jwt(token)
    #         if not user_id:
    #             await self.close(reason='User is not authenticated')
    #             return
    #         user = await sync_to_async(User.objects.get)(id=user_id)
    #         self.user = user
    #         print('HELLO USER', self.user)
    #         print('HELLO USER',user)
    #         print("ACCEPTING")
    #         await self.accept()
    #     except Exception as e:
    #         print('INVALID TOKEN',e)
    #         await self.close()

    async def disconnect(self, close_code):
        print('DISCONNECTING', close_code)
        # if self.room_group_name:
        #     await self.channel_layer.group_discard(
        #         self.room_group_name,
        #         self.channel_name
        #     )

    async def receive(self, text_data):
        #from api.utils import get_user_from_jwt
        try:
            data = json.loads(text_data)
            print(self.scope['user'])
            #token = data.get('token')
            #print('TOKEN', token)
            #user_id = get_user_from_jwt(token)
            #if not user_id:
                #await self.send(text_data=json.dumps({'error': 'User is not authenticated'}))
            
            message = "hello"
            await self.send(text_data=json.dumps({'user_id': self.scope['user'].id}))
        except json.JSONDecodeError as e:
            print('INVALID JSON', e)
            await self.send(text_data=json.dumps({'error': 'Invalid JSON'}))

        # await self.channel_layer.group_send(
        #     self.room_group_name,
        #     {
        #         'type': 'chat_message',
        #         'message': message
        #     }
        # )

    async def chat_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))