from flask import Flask, send_from_directory, abort


#############  IMPORTS  #################
from user import login, logout, signup




#############  ROUTES  #################

@post("/signup")
def _signup():
    print("ok")

@post("/login")
def _login():
    print("ok")

@post("/logout")
def _logout():
    print("ok")


#############  TEST ROUTE  #################

@app.route("/test-route")
def test_route():
    return "OK"


############### RUN #####################
app = Flask(__name__)
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=7878, debug=True)

