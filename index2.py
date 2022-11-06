# import Flask 'module'
from flask import Flask, render_template

# this will make a server application
app = Flask(__name__)

# this will define resources according to the route.
#Flask will automatically call the fucntion
@app.route("/")
def hello():
    name="Rohab"
    return render_template("home.html",name2=name)


if __name__ == "__main__":
    app.run(
    debug= True,
    host = "0.0.0.0", # this defines that the application is to be run on the local machine only. Hence localhost
    port = 3000 ) # this is the port number that the app runs on.