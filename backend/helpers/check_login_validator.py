from flask import make_response
import jwt
from . import g_keys
from database.database_queries import user_exists
def _check_login_validator(cookie_check):
    try:
        
        print("I am here")
        # Decode the token using the secret key and HS256 algorithm
        token_data = jwt.decode(cookie_check, g_keys.SECRET_KEY, algorithms=["HS256"])
        user_email = token_data["email"]
        print(user_email)
        
        user = user_exists._user_exist(user_email)
        print("user", user)
        
        if user:
            response = make_response({"user_email": user_email})
            response.status_code = 200  
            return response
        else:
            return None
    
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