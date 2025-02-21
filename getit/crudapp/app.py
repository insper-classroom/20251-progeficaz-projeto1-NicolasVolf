from flask import Flask,render_template,request,redirect,url_for,flash
import sqlite3 as sql
app=Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    con=sql.connect("db_web.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from texto")
    data=cur.fetchall()
    return render_template("index.html",datas=data)


@app.route("/submit",methods=['POST'])
def add_text():
    texto=request.form['titulo']
    detalhes=request.form['detalhes']
    con=sql.connect("db_web.db")
    cur=con.cursor()
    cur.execute("insert into texto(TITLE,DESCRICAO) values (?,?)",(texto,detalhes))
    con.commit()
    flash('User Added','success')
    return redirect('/')

    
@app.route("/delete/<int:id>",methods=['POST'])
def delete_note(id):
    con=sql.connect("db_web.db")
    cur=con.cursor()
    cur.execute("delete from texto where ID=?",(id,))
    con.commit()
    flash('Note Deleted','warning')
    return redirect(url_for("index"))
    

@app.route("/edit/<int:id>", methods=['POST'])
def edit_note(id):
    con = sql.connect("db_web.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from texto where ID = ?", (id,))
    note = cur.fetchone()
    con.close()
    return render_template("edit.html", note=note)


@app.route("/update/<int:id>",methods=['POST'])
def update_note(id):
    id = request.form['id']
    titulo = request.form['titulo']
    detalhes = request.form['detalhes']
    con = sql.connect("db_web.db")
    cur = con.cursor()
    cur.execute("UPDATE texto SET TITLE=?, DESCRICAO=? WHERE ID=?", (titulo, detalhes, id))
    con.commit()
    flash('Note Updated', 'info')
    return redirect(url_for("index"))


if __name__=='__main__':
    app.secret_key='admin123'
    app.run(debug=True)