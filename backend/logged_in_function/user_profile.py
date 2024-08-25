from flask import make_response, jsonify
from helpers import user_validation

def _user_profile():
    try:
       check_user = user_validation._user_validation()
       
       if check_user:
           user_data = {
               "user_email": check_user[1],
               "time_created": check_user[3]
           }
           return user_data
       else:
           return None
        

    except Exception as ex:
        print(ex)
        response = make_response('Error occured')
        response.status_code = 400
        return response
    
    