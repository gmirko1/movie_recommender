from flask import make_response
from helpers import cookie_validator, check_login_validator

def _home():
    cookie_check = cookie_validator._cookie_validator()
    check_login_validator._check_login_validator(cookie_check)
    
    #check if user exists in db
    
    return make_response('', 200)
