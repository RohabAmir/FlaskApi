# import Flask 'module'
from flask import Flask

# this will make a server application
app = Flask(__name__)

# this will define resources according to the route.
@app.route("/")
def hello():
    return "Hello World!";

# this will define resources according to the route.

@app.route("/mynetwork")
def mynetwork():
    return "Hello mynetwork!";

# this will define resources according to the route.
@app.route("/jobs")
def jobs():
    return "Hello jobs!";

#
if __name__ == "__main__":
    app.run(
    debug = True,
    host = "0.0.0.0", # this defines that the application is to be run on the local machine only. Hence localhost
    port = 3000) # this is the port number that the app runs on.