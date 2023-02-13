from flask import Flask, render_template
app = Flask(__name__)   #variabile identificativa del server web

@app.route('/')
def home():
  return("<h1>HOMEPAGE</h1>")

@app.route('/en')
def hello_world():
  return render_template("index.html", Titolo='Welcome', Testo='Hello, world!')

@app.route('/it')
def ciao_mondo():
  return render_template("index.html", Titolo='Benvenuti', Testo='Ciao, mondo!')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)   #codici per eseguire il server web

#indirizzo IP del nostro computer: 0.0.0.0 