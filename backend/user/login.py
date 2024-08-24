
from flask import request, make_response
from helpers import create_login_token, g_keys
from database.database_queries import user_exists, get_user
import bcrypt

def _login():
    try:
        request_user_data = request.json
    
        user_email = request_user_data["email"]
        user_password = request_user_data["password"]
        password_encode = user_password.encode('utf-8')
        
        
        check_password = user_exists._user_exist(user_email)
        if check_password:
            password_user_db = check_password[2]
            password_db_encoded = password_user_db.encode('utf-8')
            password_matched = bcrypt.checkpw(password_encode, password_db_encoded)
            
            if password_matched:
                user_checked = get_user._get_user(user_email,password_user_db )
                if user_checked:
                    #create login token for the cookie
                    jwt_cookie_token = create_login_token._generate_token(user_email)
                    
                    resp = make_response('Cookie is set')
                    resp.set_cookie(
                        'token',                      
                        jwt_cookie_token,             
                        path='/',                      
                        httponly=True,                
                        secure=False,                 
                        samesite='Lax'                
                    )
                    return resp
                else:
                    return None
            else:
                return None
        else: 
            return None
       
    except Exception as ex:
        print("Login error:", ex)
        return None



    












    