from flask import Flask, make_response
from waitress import serve
from src.strava_data import process

app = Flask(__name__, template_folder=".")

@app.route("/")
def index():
    data = process()
    response = make_response({"data": data})
    response.headers['Access-Control-Allow-Origin'] = '*' 
    return response


if __name__ == "__main__":
    print("Starting server!")
    serve(app, host="0.0.0.0", port=81)
    #app.run(host="127.0.0.1", port=8080, debug=True)