from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to Flask! This is a test of basic functions."

@app.route("/index")
def index():
    return "Welcome to Index."

if __name__ == "__main__":
    app.run(debug=True)