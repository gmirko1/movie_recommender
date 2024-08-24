from flask import request, make_response
import uuid
import bcrypt

from database.database_queries import save_user

def _signup():
    try:
        request_user_data = request.json
        user_id = str(uuid.uuid4())
        user_email = request_user_data["email"]
        user_password = request_user_data["password"]
        password_encode = user_password.encode('utf-8')
        
        
        
        salt = bcrypt.gensalt()
        password_encode = user_password.encode('utf-8')
        password_hashed = bcrypt.hashpw(password_encode, salt)
        
        print(user_email)
        print(user_password)
        print(password_encode)
        print(password_hashed)
        print("here")
        save_user._save_user(user_id, user_email, password_hashed)
        
        resp = make_response('User is created')
        return resp
        
        
    except Exception as ex:
        print("Signup error:", ex)
        return None
