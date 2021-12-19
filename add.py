from config import *



@app.route('/add_tipo_disp',methods=['POST'])
def add_tipo_disp():
    if request.method == 'POST':
        rf  = request.form
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Tipo_Dispositivo(descricao) VALUES (%s)", \
            [rf['desc']])
        mysql.connection.commit()
        cur.close()
        flash("Tipo Adicionado com Sucesso!")
    return redirect(url_for('listar_tipo_dispositivo'))



@app.route('/add_localizacao',methods=['POST'])
def add_localizacao():
    if request.method == 'POST':
        rf  = request.form
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Localizacao(descricao) VALUES (%s)", \
            [rf['desc']])
        mysql.connection.commit()
        cur.close()
        flash("Localizacao Adicionada com Sucesso!")
    return redirect(url_for('listar_localizacao'))



@app.route('/add_dispositivo',methods=['POST'])
def add_dispositivo():
    if request.method == 'POST':
        rf  = request.form
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Dispositivo(estado,estimativa_de_entrega,tipo_dispositivo,localizacao_atual) VALUES (%s,%s,%s,%s)", \
            ('Funcional',0,rf['tipo'],rf['localizacao']))
        mysql.connection.commit()
        cur.close()
        flash("Dispositivo Adicionado com Sucesso!")
    return redirect(url_for('listar_dispositivo'))



@app.route('/add_tipo_recurso_humano',methods=['POST'])
def add_tipo_recurso_humano():
    if request.method == 'POST':
        rf  = request.form
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Tipo_Recurso_Humano(descricao) VALUES (%s)", \
            [rf['desc']])
        mysql.connection.commit()
        cur.close()
        flash("Tipo Adicionado com Sucesso!")
    return redirect(url_for('listar_tipo_recurso_humano'))




@app.route('/add_especialidade',methods=['POST'])
def add_especialidade():
    if request.method == 'POST':
        rf  = request.form
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Especialidade(descricao) VALUES (%s)", \
            [rf['desc']])
        mysql.connection.commit()
        cur.close()
        flash("Especialidade Adicionada com Sucesso!")
    return redirect(url_for('listar_especialidade'))




@app.route('/add_recurso_humano',methods=['POST'])
def add_recurso_humano():
    print("\n\nVOU DAR DATA\n\n")
    if request.method == 'POST':
        rf  = request.form
        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO Recurso_Humano(nome,data_nascimento,tipo_recurso,especialidade)
            VALUES (%s,%s,%s,%s)
            """, [rf['nome'],rf['data'],rf['tipo'],rf['especialidade']])
        mysql.connection.commit()
        cur.close()
        flash("Recurso Adicionado com Sucesso!")
    return redirect(url_for('listar_recurso_humano'))




@app.route('/add_deslocacao/<id>',methods=['POST'])
def add_deslocacao(id):
    if request.method == 'POST':
        rf  = request.form
        cur = mysql.connection.cursor()

        cur.execute("SELECT localizacao_atual FROM Dispositivo WHERE id_Dispositivo = %s",[id])
        x = cur.fetchall()
        
        cur.execute("""
            INSERT INTO Deslocacao(data,dispositivo,responsavel,localizacao_origem,localizacao_destino)
            VALUES (%s,%s,%s,%s,%s)
            """, [rf['data'],id,rf['responsavel'],x[0],rf['loc_destino']])

        cur.execute("UPDATE Dispositivo SET localizacao_atual = %s WHERE id_Dispositivo  = %s", \
            (rf['loc_destino'],id))

        mysql.connection.commit()
        cur.close()
        flash("Deslocacao Adicionada com Sucesso!")
    return redirect(url_for('listar_dispositivo'))




@app.route('/add_permissao',methods=['POST'])
def add_permissao():
    if request.method == 'POST':
        rf  = request.form
        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT IGNORE INTO Recurso_Humano_manipula_Tipo_Dispositivo(id_Recurso_Humano,id_Tipo_Dispositivo)
            VALUES (%s,%s)
            """, [rf['responsavel'],rf['tipo']])
        mysql.connection.commit()
        cur.close()
        flash("Permissão Adicionada com Sucesso!")
    return redirect(url_for('listar_permissoes'))