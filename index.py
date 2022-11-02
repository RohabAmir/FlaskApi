# import Flask 'module'
from flask import Flask, render_template

# this will make a server application
app = Flask(__name__)

# this will define resources according to the route.
#Flask will automatically call the fucntion
@app.route("/")
def hello():
    return render_template("home.html")

# this will define resources according to the route.

# @app.route("/mynetwork")
# def mynetwork():
    # if (user.name == "rohab")
    #    result = searchInDatabase("rohab")
    #    result = {
    #     name:"rohab",
    #     picture: "image.png",
    #     about: "drtyfdfg",
    #     noOfFollowers: "scdasdf",
    #     password: '',
    #     phoneNumber: '',
    #     location: 
    #    }
    return result;


# @app.route("/post") # searched by => id = 1234
# def post():
#     result = searchInDatabase("1234")
#     result = {
#         user: "rohab",
#         picture: ["image.png", "image.png", "image.png"],
#         text: "drtyfdfg",
#         noOfLikes: 12,
#         noOfComments 123,
#     }
#     return result;

# this will define resources according to the route.
@app.route("/jobs")
def jobs():
    return "Hello jobs!";

# @app.route("/home")
# def home():
#     """View for the Home page of the website."""
#     return "Welcome to the HomePage!"



n=4
@app.route("/pattern")
def getPattern():
    for i in range (n):
        print("*" * n)
    return " SQAURE PATTERN IS PRINTED ON THE TERMINAL"

"""An example application to demonstrate Variable Rules in Routing"""

@app.route("/<my_name>")
def greatings(my_name):
    """View function to greet the user by name."""
    return "Welcome "+ my_name +"!"


"""An example application to demonstrate Dynamic Routing"""

@app.route('/square/<int:number>')
def show_square(number):
    """View that shows the square of the number passed by URL"""
    return "Square of "+ str(number) +" is: "+ str(number * number) 


"""1. Add a View Function for the Home page."""

@app.route('/Home')
def homePage():
    return "Paws Rescue Center 🐾"

"""2. Add a View Function for the About page."""

@app.route('/About')
def AboutPage():
    return """We are a non-profit organization working as an animal rescue. We aim to help you connect with the purrfect furbaby for you! The animals you find on our website are rescued and rehabilitated animals. Our mission is to promote the ideology "adopt, don't hop"! """






if __name__ == "__main__":
    app.run(
    debug= True,
    host = "0.0.0.0", # this defines that the application is to be run on the local machine only. Hence localhost
    port = 3000 ) # this is the port number that the app runs on.