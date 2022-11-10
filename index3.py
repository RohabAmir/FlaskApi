from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    Users = {
                "Rohab":"Sabzazar", 
                "Ahmed":"Gulshan e Ravi", 
                "Tabish":"EME", 
                "Abuzar":"Awan Town"
            }
    return render_template("home1.html", users=Users)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)