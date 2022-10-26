from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!";

@app.route("/mynetwork")
def hello():
    return "Hello mynetwork!";

@app.route("/jobs")
def hello():
    return "Hello jobs!";


if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 3000)