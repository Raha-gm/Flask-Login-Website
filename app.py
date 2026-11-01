from flask import *

# Create the Flask application
app = Flask(__name__)


# Homepage route
@app.route("/")
def home():
    return render_template("index.html")


# Buy page route
@app.route("/buy")
def call():
    return render_template("call.html")


# Login page route
@app.route("/login")
def login():
    return render_template("login.html")


# Run the application
if __name__ == "__main__":
    app.run(debug=True)