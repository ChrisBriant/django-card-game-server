from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import UntypedToken
#from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

def get_user_id_from_jwt(token):
    try:
        #User = get_user_model()
        # Attempt to validate the token
        print('TOKEN RECIEVED IS', token)
        validated_token = UntypedToken(token)
        print('VALIDATED TOKEN', validated_token.payload)
        #JWTAuthentication().authenticate_credentials(validated_token)
        #user = Token.objects.get(key=validated_token).user
        #print("USER",user)
        #user = User.objects.get(id=validated_token.payload.get('user_id'))
        
        # If authentication is successful, return the user
        return validated_token.payload.get('user_id')
        #return user
    
    except InvalidToken as e:
        print("Token is invalid", e)
        # Token is invalid
        return None
    
    except TokenError as e:
        print("Token Error", e)
        # Token is malformed or other TokenError
        return None