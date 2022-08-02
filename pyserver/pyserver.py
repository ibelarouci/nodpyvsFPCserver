from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Pong</h1>"

if __name__ == "__main__":
    print("Server running on localhost:9002")
    from waitress import serve
    serve(app, host="0.0.0.0", port=9002)

