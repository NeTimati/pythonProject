from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Мое первое приложение на фласке!</h1>'  '<p> <h1>Вторая строчка </h1> </p>'\
    '<table><table border =#><tr><td>ячейка 1</td><td>ячейка 2 </td></table>'

@app.route('/privet')
def greeting():
    return '<h1>Мое первое приложение на фласке!</h1>'  '<p> <h1>Вторая строчка </h1> </p>'


if __name__ == '__main__':
    app.run(debug = True)
