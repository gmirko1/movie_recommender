from flask import Flask, jsonify, make_response
app = Flask(__name__)

#############  IMPORTS  #################
from user import login, logout, signup
from logged_in_function import home


#############  TEST ROUTE  #################

@app.route("/test-route")
def test_route():
    return "OK"

#############  ROUTES  #################

def _auth_routes(app):
    @app.route('/api/signup/', methods=['POST'])
    def _signup():
        try:
            response_signup = signup._signup()
            return response_signup
        except Exception as ex:
            print(ex)
            return make_response("Error occured"), 500

    @app.route('/api/login/', methods=['POST'])
    def _login():
        try:
            response_login = login._login()
            return response_login
        except Exception as ex:
            print(ex)
            return make_response("Error occured"), 500

    @app.route('/api/logout', methods=['POST'])
    def _logout():
        try:
            response_logout = logout._logout()
            return response_logout
        except Exception as ex:
            print(ex)
            return make_response("Error occured"), 500

def _user_routes(app):
    @app.route('/api/home/', methods = ['GET'])
    def _home():
        try:
            response_home = home._home()
        
            if response_home is not None:
                response = make_response('Check sucessfull')
                response.status_code = 200  
                return response
            else:
                response = make_response('Error occured')
                response.status_code = 400
                return response
            
            
        except Exception as ex:
            print(ex)
            return make_response("Error occured"), 500


