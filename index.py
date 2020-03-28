from flask import Flask, render_template, request
import re

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('Index.html')


@app.route('/about')
def adout():
    return 'hello 2'


@app.route('/validador', methods=['POST'])
def validar():

    if request.method == 'POST':
        expresion = request.form['expre']
        if expresion == '':
            return render_template('vacio.html')

        patron = re.compile("[A-Z]{1}[0-9]{3}[a-z]{3}[\W]{3}")

        if patron.search(expresion):
            resultado = patron.search(expresion).group(0)
            if resultado == expresion:
                return render_template('correcta.html')
            else:
                return render_template('incorrecta.html')
        else:
            return render_template('incorrecta.html')


if __name__ == '__main__':
    app.run(debug=True)
