from flask import make_response
from . import cookie_validator
from . import check_login_validator



def _user_validation():
    try:
        cookie_check = cookie_validator._cookie_validator()
        
        
        if cookie_check:
            check_login = check_login_validator._check_login_validator(cookie_check)
            return check_login
        else:
            return None

    except Exception as ex:
        print(f"Error occurred: {ex}")
        response = make_response('Error occurred')
        response.status_code = 400
        return response