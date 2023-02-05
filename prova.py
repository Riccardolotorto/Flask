from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def benvenuto():
    return ('<h1>BENVENUTO</h1>')

@app.route('/en', methods=['GET'])
def hello_world():
    return ('<h1>Hello, world!</h1>')

@app.route('/contatti', methods=['GET'])
def contatti():
    return ('<h1>Contattami! Mi chiamo Riccardo Lotorto</h1>')

@app.route('/inter', methods=['GET'])
def inter():
    return ('<h1>Tifo inter</h1>')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)