from flask import Flask

#############  FLASK APP   #################
app = Flask(__name__)


############### ROUTES #####################
from routes import _auth_routes, _user_routes, _media_library
_auth_routes(app)
_user_routes(app)
_media_library(app)


############### RUN #####################

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5001, debug=True)

