from flask import make_response

def _logout():
    try:
        response = make_response("Logged out successfully")
        response.delete_cookie('token', path='/', httponly=True)
        response.status_code = 200
        return response
    except Exception as ex:
        print("Logout error:", ex)
        response = make_response("An error occurred")
        response.status_code = 500
        return response
    
