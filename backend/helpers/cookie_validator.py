from flask import request, make_response

def _cookie_validator():
    cookie = request.cookies.get("token")
    
    if cookie:
        response = make_response(cookie)
        response.status_code = 200
        return response
    else:
        response = make_response("Cookie not found")
        response.status_code = 400
        return response
