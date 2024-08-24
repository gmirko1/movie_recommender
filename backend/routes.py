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
    @app.route('/api/signup', methods=['POST'])
    def _signup():
        try:
            print("Here")
        except Exception as ex:
            print(ex)
            return jsonify(error="Error occured", message=str(ex)), 500

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
            return response_home
        except Exception as ex:
            print(ex)
            return make_response("Error occured"), 500


