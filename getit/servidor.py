from flask import Flask, render_template_string, request, redirect, render_template
import sqlite3 as sql

import views


app = Flask(__name__)

# Configurando a pasta de arquivos estáticos
app.static_folder = 'static'

@app.route('/')
def index():
    con=sql.connect("db_web.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from texto")
    data=cur.fetchall()
    return render_template("index.html",datas=data)

@app.route('/submit', methods=['POST'])
def submit_form():
    titulo = request.form.get('titulo')  # Obtém o valor do campo 'titulo'
    detalhes = request.form.get('detalhes')  # Obtém o valor do campo 'detalhes'

    views.submit(titulo, detalhes)
    return redirect('/')

@app.route('/delete/<int:id>', methods=['POST'])
def delete_notess(id):
    print(id)
    con = sql.connect("db_web.db")
    cur = con.cursor()
    cur.execute("DELETE FROM texto WHERE id = ?", (id,))
    con.commit()
    con.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)