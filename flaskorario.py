from flask import Flask, render_template
app = Flask(__name__)

import datetime 
adesso_orario = int((datetime.datetime.now().time().hour))
print(adesso_orario)


@app.route("/")
def saluto():
    if adesso_orario >= 12:
        return render_template("orario.html", Titolo = "Buonasera", Immagine = "https://www.bgiorno.it/wp-content/uploads/2020/03/Immagini-Buonasera-1.jpg")
    else:
        return render_template("orario.html", Titolo = "Buongiorno", Immagine = "https://immaginissime.it/wp-content/uploads/2022/11/photo1666478621.jpeg")

@app.route("/en")
def hello():
    if adesso_orario >= 12:
        return render_template("orario.html", Titolo = "Good evening", Immagine = "https://www.bgiorno.it/wp-content/uploads/2020/03/Immagini-Buonasera-1.jpg")
    else:
        return render_template("orario.html", Titolo = "Good morning", Immagine = "https://immaginissime.it/wp-content/uploads/2022/11/photo1666478621.jpeg")
        


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)