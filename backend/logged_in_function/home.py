from flask import make_response
from helpers import user_validation

def _home():
    try:
        response = user_validation._user_validation()
        return response 
    except Exception as ex:
        print(ex)
        response = make_response('Error occured')
        response.status_code = 400
        return response
    
    