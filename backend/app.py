from flask import Flask

#############  FLASK APP   #################
app = Flask(__name__)


############### ROUTES #####################
from routes import _auth_routes
_auth_routes(app)


############### RUN #####################

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5001, debug=True)

