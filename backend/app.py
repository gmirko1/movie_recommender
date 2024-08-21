from flask import Flask, send_from_directory, abort

app = Flask(__name__)

#############  IMAGES  #################

@app.route("/test-route")
def test_route():
    return "OK"


############### RUN #####################

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=7878, debug=True)

