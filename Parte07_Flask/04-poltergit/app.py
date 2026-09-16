from flask import Flask, render_template, request
import pyautogui as auto

from dateime import date 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/comitar" , methods = ["POST"])
def comitar():
    hoje = date.today().strftime("%d/%m/%Y")
    msg = None
    repositorio = None
    if request.method == 'POST':
        repositorio = request.form['repositorio']
    return render_template('index.html')
    auto.PAUSE = 1
    auto.hotkey('win', 'r')
    auto.write('cmd')
    auto.press('enter')
    auto.write(f"cd {repositorio}")"
    auto.press('enter')
else:
    msg = "Repositorio invalido.
    return render_template("index.html")"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)