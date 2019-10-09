from flask import Flask, render_template

app = Flask(__name__)
nome_app = "Mercado Tech"


@app.route('/')
def inicio():
    return render_template('index.html', n_app = nome_app)

@app.route('/cervejas')
def cervejas():
    return render_template('cervejas.html', n_app = nome_app)


app.run()