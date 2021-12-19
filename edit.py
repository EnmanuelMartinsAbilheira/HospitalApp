from config import *



@app.route('/edit_tipo_disp/<id>')
def get_tipo_disp(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Tipo_Dispositivo WHERE id_Tipo_Dispositivo = %s",[id])
    x = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template("edit_tipo_disp.html",x=x[0])


@app.route('/update_tipo_disp/<id>',methods=['POST'])
def update_tipo_disp(id):
    if request.method=='POST':
        desc  = request.form['desc']
        cur = mysql.connection.cursor()
        cur.execute("""

            UPDATE Tipo_Dispositivo SET
                descricao  = %s
            WHERE id_Tipo_Dispositivo  = %s

        """,(desc,id))
        mysql.connection.commit()
        cur.close()
        flash("Tipo de Dispositivo Atualizado com Sucesso!")
        return redirect(url_for('listar_tipo_dispositivo'))



@app.route('/edit_localizacao/<id>')
def get_localizacao(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Localizacao WHERE id_Localizacao = %s",[id])
    x = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template("edit_localizacao.html",x=x[0])


@app.route('/update_localizacao/<id>',methods=['POST'])
def update_localizacao(id):
    if request.method=='POST':
        desc  = request.form['desc']
        cur = mysql.connection.cursor()
        cur.execute("""

            UPDATE Localizacao SET
                descricao  = %s
            WHERE id_Localizacao  = %s

        """,(desc,id))
        mysql.connection.commit()
        cur.close()
        flash("Localizacao Atualizada com Sucesso!")
        return redirect(url_for('listar_localizacao'))



@app.route('/edit_tipo_recurso_humano/<id>')
def get_tipo_recurso_humano(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Tipo_Recurso_Humano WHERE id_Tipo_Recurso_Humano = %s",[id])
    x = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template("edit_tipo_recurso_humano.html",x=x[0])


@app.route('/update_tipo_recurso_humano/<id>',methods=['POST'])
def update_tipo_recurso_humano(id):
    if request.method=='POST':
        rf  = request.form
        cur = mysql.connection.cursor()
        cur.execute("""

            UPDATE Tipo_Recurso_Humano SET
                descricao = %s
            WHERE id_Tipo_Recurso_Humano = %s

        """,(rf['desc'],id))
        mysql.connection.commit()
        cur.close()
        flash("Tipo de Recurso Humano Atualizado com Sucesso!")
        return redirect(url_for('listar_tipo_recurso_humano'))



@app.route('/edit_especialidade/<id>')
def get_especialidade(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Especialidade WHERE id_Especialidade = %s",[id])
    x = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template("edit_especialidade.html",x=x[0])


@app.route('/update_especialidade/<id>',methods=['POST'])
def update_especialidade(id):
    if request.method=='POST':
        rf  = request.form
        cur = mysql.connection.cursor()
        cur.execute("""

            UPDATE Especialidade SET
                descricao = %s
            WHERE id_Especialidade = %s

        """,(rf['desc'],id))
        mysql.connection.commit()
        cur.close()
        flash("Especialidade Atualizada com Sucesso!")
        return redirect(url_for('listar_especialidade'))



@app.route('/edit_recurso_humano/<id>')
def get_recurso_humano(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Recurso_Humano WHERE id_Recurso_Humano = %s",[id])
    x = cur.fetchall()
    cur.execute("SELECT descricao FROM Tipo_Recurso_Humano WHERE id_Tipo_Recurso_Humano = %s",str(x[0][3]))
    t = cur.fetchall()
    cur.execute("SELECT descricao FROM Especialidade WHERE id_Especialidade = %s",str(x[0][4]))
    e = cur.fetchall()
    cur.execute("SELECT * FROM Tipo_Recurso_Humano")
    ts = cur.fetchall()
    cur.execute("SELECT * FROM Especialidade")
    es = cur.fetchall()
    
    mysql.connection.commit()
    cur.close()
    return render_template("edit_recurso_humano.html",x=x[0],Tipo=t[0][0],Especialidade=e[0][0],Tipos=ts,Especialidades=es)


@app.route('/update_recurso_humano/<id>',methods=['POST'])
def update_recurso_humano(id):
    if request.method=='POST':
        rf  = request.form
        cur = mysql.connection.cursor()
        cur.execute("""

            UPDATE Recurso_Humano SET
                nome  = %s,
                data_nascimento = %s,
                tipo_recurso = %s,
                especialidade = %s
            WHERE id_Recurso_Humano  = %s

        """,(rf['nome'],rf['data'],rf['tipo'],rf['especialidade'],id))
        mysql.connection.commit()
        cur.close()
        flash("Recurso Humano Atualizado com Sucesso!")
        return redirect(url_for('listar_recurso_humano'))
