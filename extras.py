from config import *



@app.route('/usar_dispositivo/<id>',methods=['GET'])
def usar_dispositivo(id):
    if request.method=='GET':
        rf  = request.form
        cur = mysql.connection.cursor()

        cur.execute("SELECT estado FROM Dispositivo WHERE id_Dispositivo = %s",[id])
        e = cur.fetchall()[0][0]
        if e=="Funcional":
            cur.execute("UPDATE Dispositivo SET estado  = %s WHERE id_Dispositivo  = %s",\
                ('Não Funcional',id))
        else:
            flash("Não foi possivel (Dispositivo precisa de ser Reparado)")
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('listar_dispositivo'))

@app.route('/iniciar_reparacao/<id>',methods=['POST'])
def iniciar_reparacao(id):
    if request.method=='POST':
        rf  = request.form
        cur = mysql.connection.cursor()
        cur.execute("UPDATE Dispositivo SET estado = %s,estimativa_de_entrega = %s WHERE id_Dispositivo = %s",\
            ('Em Reparação',rf['estim'],id))
        mysql.connection.commit()
        cur.close()
        flash("Iniciado o processo de Reparação")
        return redirect(url_for('sala_de_reparacoes'))


@app.route('/reparar_dispositivo/<id>',methods=['GET'])
def reparar_dispositivo(id):
    if request.method=='GET':
        rf  = request.form
        cur = mysql.connection.cursor()

        cur.execute("SELECT localizacao_atual FROM Dispositivo WHERE id_Dispositivo = %s",[id])
        l = cur.fetchall()[0][0]
        
        cur.execute("SELECT estado FROM Dispositivo WHERE id_Dispositivo = %s",[id])
        e = cur.fetchall()[0][0]
        
        if l != 1:
            flash("Não foi possivel reparar (o Dispositivo não se encontra localizado na Sala de Reparações)")

        elif e=="Funcional":
            flash("Não foi possivel reparar (o Dispositivo já está Funcional)")
        
        elif e=='Em Reparação':
            cur.execute("UPDATE Dispositivo SET estado = %s,estimativa_de_entrega = %s WHERE id_Dispositivo = %s",('Funcional',0,id))
            flash("Dispositivo foi reparado com Sucesso!")

        else:
            cur.close()
            return render_template("estimativa_entrega.html",Id=id)
            
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('sala_de_reparacoes'))



@app.route('/mover_dispositivo/<id>',methods=['GET'])
def mover_dispositivo(id):
    if request.method=='GET':
        rf  = request.form
        cur = mysql.connection.cursor()

        cur.execute("SELECT tipo_dispositivo FROM Dispositivo WHERE id_Dispositivo = %s",[id])
        x = cur.fetchall()[0]

        cur.execute("""

            SELECT * FROM Recurso_Humano WHERE id_Recurso_Humano
            IN (SELECT id_Recurso_Humano 
                FROM Recurso_Humano_manipula_Tipo_Dispositivo
                WHERE id_Tipo_Dispositivo = %s)
            
            """,x)
        
        res = cur.fetchall()
                
        cur.execute("SELECT * FROM Localizacao")
        ls = cur.fetchall()

        mysql.connection.commit()
        cur.close()
        return render_template('mover_dispositivo.html',Responsaveis=res,Localizacoes=ls,Id=id)