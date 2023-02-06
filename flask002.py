from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return("<h1>prova</h1>")

@app.route('/en')
def hello_world():
  return render_template("indexcss.html", Titolo='Welcome', Testo='Hello, world!', Immagine = "https://www.olio-extra-vergine.it/images/articoli/Olio-Brexit.png")

@app.route('/it')
def ciao_mondo():
  return render_template("indexcss.html", Titolo='Benvenuti', Testo='Ciao, mondo!', Immagine = "https://static.geopop.it/wp-content/uploads/sites/32/2022/05/iStock-1212397487.jpg")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

