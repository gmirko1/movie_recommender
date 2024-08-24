
from flask import request, make_response
from helpers import create_login_token, g_keys

def _login():
    try:
        request_user_data = request.json
    
        user_email = request_user_data["email"]
        user_password = request_user_data["password"]
        password_encode = user_password.encode('utf-8')
        
        
        #check if email exists
        
        
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
    except Exception as ex:
        print("Login error:", ex)
        return None

    
    












    