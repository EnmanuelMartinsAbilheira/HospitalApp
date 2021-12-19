from config import *



@app.route('/listar_tipo_dispositivo')
def listar_tipo_dispositivo():
    cur = mysql.connection.cursor()
    utilizadores = cur.execute("SELECT * FROM Tipo_Dispositivo")
    dados=cur.fetchall()
    cur.close()
    return render_template("list_tipo_dispositivo.html",Dados=dados)



@app.route('/listar_localizacao')
def listar_localizacao():
    cur = mysql.connection.cursor()
    utilizadores = cur.execute("SELECT * FROM Localizacao")
    dados=cur.fetchall()
    cur.close()
    return render_template("list_localizacao.html",Dados=dados)



@app.route('/listar_dispositivo')
def listar_dispositivo():
    cur = mysql.connection.cursor()
    cur.execute("""
    	
        SELECT id_Dispositivo,estado,estimativa_de_entrega,T.descricao,L.descricao FROM Dispositivo
    	INNER JOIN Tipo_Dispositivo as T ON tipo_dispositivo = id_Tipo_Dispositivo
    	INNER JOIN Localizacao as L ON localizacao_atual = id_Localizacao

        """)
    dados=cur.fetchall()
    cur.execute("SELECT * FROM Tipo_Dispositivo")
    tipos = cur.fetchall()
    cur.execute("SELECT * FROM Localizacao")
    localizacoes = cur.fetchall()
    cur.close()
    return render_template("list_dispositivo.html",Dados=dados \
    	,Tipos=tipos, Localizacoes=localizacoes)



@app.route('/listar_tipo_recurso_humano')
def listar_tipo_recurso_humano():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Tipo_Recurso_Humano")
    dados=cur.fetchall()
    cur.close()
    return render_template("list_tipo_recurso_humano.html",Dados=dados)



@app.route('/listar_especialidade')
def listar_especialidade():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Especialidade")
    dados=cur.fetchall()
    cur.close()
    return render_template("list_especialidade.html",Dados=dados)




@app.route('/listar_recurso_humano')
def listar_recurso_humano():
    cur = mysql.connection.cursor()
    cur.execute("""

        SELECT id_Recurso_Humano,nome,data_nascimento,T.descricao,E.descricao FROM Recurso_Humano
        INNER JOIN Tipo_Recurso_Humano as T ON tipo_recurso = id_Tipo_Recurso_Humano
        INNER JOIN Especialidade as E ON especialidade = id_Especialidade

        """)
    dados=cur.fetchall()
    cur.execute("SELECT * FROM Tipo_Recurso_Humano")
    tipos = cur.fetchall()
    cur.execute("SELECT * FROM Especialidade")
    esps = cur.fetchall()
    cur.close()
    return render_template("list_recurso_humano.html",Dados=dados,Tipos=tipos,Especialidades=esps)




@app.route('/listar_deslocacao')
def listar_deslocacao():
    cur = mysql.connection.cursor()
    cur.execute("""

        SELECT id_Deslocacao,data,dispositivo,R.nome,O.descricao,D.descricao,T.descricao FROM Deslocacao
        INNER JOIN Recurso_Humano as R ON responsavel = id_Recurso_Humano
        INNER JOIN Localizacao as O ON localizacao_origem = O.id_Localizacao
        INNER JOIN Localizacao as D ON localizacao_destino = D.id_Localizacao
        INNER JOIN Dispositivo as Disp ON dispositivo = Disp.id_Dispositivo
        INNER JOIN Tipo_Dispositivo as T ON Disp.tipo_dispositivo = T.id_Tipo_Dispositivo
        ORDER BY data DESC

        """)
    dados=cur.fetchall()

    
    cur.close()
    return render_template("list_deslocacao.html",Dados=dados)




@app.route('/listar_permissoes')
def listar_permissoes():
    cur = mysql.connection.cursor()
    cur.execute("""

        SELECT P.id_Recurso_Humano,R.nome,P.id_Tipo_Dispositivo,T.descricao FROM Recurso_Humano_manipula_Tipo_Dispositivo as P
        INNER JOIN Recurso_Humano as R ON P.id_Recurso_Humano = R.id_Recurso_Humano
        INNER JOIN Tipo_Dispositivo as T ON P.id_Tipo_Dispositivo = T.id_Tipo_Dispositivo
        ORDER BY P.id_Recurso_Humano ASC

        """)
    dados=cur.fetchall()
    cur.execute("SELECT id_Tipo_Dispositivo,descricao FROM Tipo_Dispositivo")
    ts = cur.fetchall()
    cur.execute("SELECT id_Recurso_Humano,nome FROM Recurso_Humano")
    rs = cur.fetchall()
    cur.close()
    return render_template("list_permissoes.html",Dados=dados, \
        Responsaveis=rs,Tipos=ts)


@app.route('/sala_de_reparacoes')
def sala_de_reparacoes():
    cur = mysql.connection.cursor()
    cur.execute("""
        
        SELECT id_Dispositivo,estado,estimativa_de_entrega,T.descricao,L.descricao FROM Dispositivo
        INNER JOIN Tipo_Dispositivo as T ON tipo_dispositivo = id_Tipo_Dispositivo
        INNER JOIN Localizacao as L ON localizacao_atual = id_Localizacao
        WHERE estado = 'Não Funcional' OR estado = 'Em Reparação' OR localizacao_atual = 1

        """)
    dados=cur.fetchall()
    cur.close()
    return render_template("sala_de_reparacoes.html",Dados=dados)