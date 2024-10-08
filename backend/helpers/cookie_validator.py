from flask import request, make_response
from user import logout
def _cookie_validator():
    cookie = request.cookies.get("token")
    
    if cookie:
        response = make_response(cookie)
        response.status_code = 200
        return response
    else:
        response = make_response("Logged out successfully")
        response.delete_cookie('token', path='/', httponly=True)

