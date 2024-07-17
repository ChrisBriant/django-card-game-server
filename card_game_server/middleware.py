from django.contrib.auth.models import AnonymousUser
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.authtoken.models import Token
from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware
from rest_framework_simplejwt.tokens import UntypedToken
from django.contrib.auth import get_user_model
import json

@database_sync_to_async
def get_user(token_key):
    try:
        #token = Token.objects.get(key=token_key)
        # tokens = Token.objects.all()
        # print('Are there any tokens', tokens)
        # for toki in tokens:
        #     print('Toki woki', toki)
        
        User = get_user_model()
        print('ATTEMPT TO GET USER',token_key)
        validated_token = UntypedToken(token_key)
        print('IS THERE A TOKEN', validated_token.payload)
        user_id = validated_token.payload.get('user_id')
        user = User.objects.get(id=user_id)
        print('IS THERE A USER', user)
        return user
    except TokenError as e:
        print('TOKEN ERROR', e)
        return AnonymousUser()
    except Token.DoesNotExist as e:
        print('TOKEN DOES NOT EXIST', e)
        return AnonymousUser()

class TokenAuthMiddleware(BaseMiddleware):
    def __init__(self, inner):
        super().__init__(inner)

    async def __call__(self, scope, receive, send):
        # print('WHY NO INFORMATION')
        # try:
        #     headers = dict(scope['headers'])
        #     print("HEADERS", headers)
        #     raw_token = headers.get(b'sec-websocket-protocol')
        #     if raw_token:
        #         token_key = raw_token.decode().split(' ')[1]
        #     else:
        #         token_key = None
        #     #token_key = (dict((x.split('=') for x in scope['query_string'].decode().split("&")))).get('sec-websocket-protocol', None)
        # except ValueError as e:
        #     print('VALUE ERROR', e)
        #     token_key = None
        # scope['user'] = AnonymousUser() if token_key is None else await get_user(token_key)
        # return await super().__call__(scope, receive, send)
    
        # async def token_auth_receive():
        #     message = await receive()
        #     print("message",message)
        #     await self.inner(scope, receive, send)
        # return await token_auth_receive()
    
        async def inner_receive():
            message = await receive()
            if message['type'] == 'websocket.connect':
                print('WebSocket connection received')
                await send({'type': 'websocket.accept'})
                auth_message = await receive()
                print("AUTH MESSAGE",auth_message)
                auth_data = json.loads(auth_message['text'])
                token_key = auth_data.get('token')
                scope['user'] = await get_user(token_key) if token_key else AnonymousUser()
                print('USER iS', scope['user'])
                if not scope['user'].is_authenticated:
                    await send({
                        'type': 'websocket.send',
                        'text': json.dumps({'type': 'auth', 'status': 'error', 'error': 'Invalid token'}),
                    })
                    await send({'type': 'websocket.close'})
                    return
                else:
                    await send({
                        'type': 'websocket.send',
                        'text': json.dumps({'type': 'auth', 'status': 'ok'}),
                    })
            await self.inner(scope, receive, send)

        return await inner_receive()