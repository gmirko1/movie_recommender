from flask import make_response
from helpers import cookie_validator, check_login_validator

def _home():
    try:
        cookie_check = cookie_validator._cookie_validator()
        
        if cookie_check:
            check_login = check_login_validator._check_login_validator(cookie_check)
            return check_login
        else: 
            return None

    except Exception as ex:
        print(ex)
        response = make_response('Error occured')
        response.status_code = 400
        return response
    
    