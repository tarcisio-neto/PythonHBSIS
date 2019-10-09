from flask import Flask,render_template

app = Flask(__name__)

nome_pagina = 'MercadoTech'

@app.route('/')
def inicio():
    return render_template('index.html', nome_pagina = nome_pagina)

@app.route('/produto')
def produto():
    return render_template('produtos.html', nome_pagina = nome_pagina)



app.run()