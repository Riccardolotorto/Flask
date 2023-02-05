from flask import Flask, render_template
app = app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return render_template("index.html", Titolo='Welcome', Testo='Hello, world!')

@app.route('/it', methods=['GET'])
def benvenuto():
    return render_template("index.html", Titolo='Benvenuto', Testo='Ciao mondo!')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)