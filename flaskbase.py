from flask import Flask
app = Flask(__name__)

@app.route("/", methods = ["GET"])
def home():
    return("<h1>Home</h1>")

@app.route("/it")
def ciao():
    return("<h1>Ciao Mondo!</h1>")

@app.route("/en")
def hello():
    return("<h1>Hello World!</h1>")


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)