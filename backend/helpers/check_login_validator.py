from flask import make_response
import jwt
from . import g_keys

def _check_login_validator(cookie_check):
    try:
        # Decode the token using the secret key and HS256 algorithm
        token_data = jwt.decode(cookie_check, g_keys.SECRET_KEY, algorithms=["HS256"])
        user_email = token_data["email"]
        
        # Create a response with a 200 status code
        response = make_response({"user_email": user_email})
        response.status_code = 200
        return response
    
    except jwt.ExpiredSignatureError:
        # Create a response for expired token
        response = make_response("Token is expired")
        response.status_code = 401
        return response
    
    except jwt.InvalidTokenError:
        # Create a response for invalid token
        response = make_response("Invalid token")
        response.status_code = 400
        return response