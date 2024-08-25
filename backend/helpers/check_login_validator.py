from flask import make_response
import jwt
from . import g_keys
from database.database_queries import user_exists


def _check_login_validator(cookie_check):

    try:
        token_data_extracted = cookie_check.get_data(as_text=True)
        token_data = jwt.decode(token_data_extracted, g_keys.SECRET_KEY, algorithms=["HS256"])
        user_email = token_data["email"]
        
        user = user_exists._user_exist(user_email)
        
        if user:
            response = make_response({"user_email": user_email})
            response.status_code = 200  
            return user
        else:
            return None
    
    except jwt.ExpiredSignatureError:
        response = make_response("Token is expired")
        response.status_code = 401
        return response
    
    except jwt.InvalidTokenError:
        response = make_response("Invalid token")
        response.status_code = 400
        return response