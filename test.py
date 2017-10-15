from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!!!!"

@app.route("/dicks")
def helloDicks():
    return "Hello Dickasds!"

if __name__ == "__main__":
    app.run()
