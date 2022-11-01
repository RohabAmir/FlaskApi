# import Flask 'module'
from flask import Flask

# this will make a server application
app = Flask(__name__)

# this will define resources according to the route.
#Flask will automatically call the fucntion
@app.route("/")
def hello():
    return "Hello World!";

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

@app.route("/home")
def home():
    """View for the Home page of the website."""
    return "Welcome to the HomePage!"



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



if __name__ == "__main__":
    app.run(
    host = "127.0.0.1", # this defines that the application is to be run on the local machine only. Hence localhost
    port = 5002 ) # this is the port number that the app runs on.