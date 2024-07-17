from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import UntypedToken

def get_user_from_jwt(token):
    try:
        # Attempt to validate the token
        validated_token = UntypedToken(token)
        JWTAuthentication().authenticate_credentials(validated_token)
        
        # If authentication is successful, return the user
        return validated_token.payload.get('user_id')
    
    except InvalidToken:
        # Token is invalid
        return None
    
    except TokenError:
        # Token is malformed or other TokenError
        return None