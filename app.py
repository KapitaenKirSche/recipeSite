from flask import Flask, Response, send_from_directory, send_file, request
from backend.api_functions import *

app = Flask(__name__)
app.config.from_object(__name__)

API_KEY = 'd51018ff1c584396b27aa838d2b6feb2'

@app.route("/")
def index():
    return send_file("static/index.html")

@app.route("/static/<path:path>")
def send_report(path):
    return send_from_directory("static", path)




if __name__ == "__main__":  # pragma: no cover
    print('run')
    print(search_recipes('pasta', API_KEY))
    app.run(port=8080)