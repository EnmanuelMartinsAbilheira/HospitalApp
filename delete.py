from config import *



@app.route('/delete_tipo_disp/<id>')
def delete_tipo_disp(id):
    cur = mysql.connection.cursor()

    cur.execute("SELECT COUNT(*) FROM Dispositivo WHERE tipo_dispositivo = %s",[id])
    n = int(cur.fetchall()[0][0])
    if(n>0):
        flash("Não foi possivel eliminar Tipo (está associado a pelo menos um Dispositivo)")
        return redirect(url_for('listar_tipo_dispositivo'))
    
    cur.execute("SELECT COUNT(*) FROM Recurso_Humano_manipula_Tipo_Dispositivo WHERE id_Tipo_Dispositivo = %s",[id])
    n = int(cur.fetchall()[0][0])
    if(n>0):
        flash("Não foi possivel eliminar Tipo (está associado a pelo menos uma Permissão)")
        return redirect(url_for('listar_tipo_dispositivo'))
    
    cur.execute("DELETE FROM Tipo_Dispositivo WHERE id_Tipo_Dispositivo = %s",[id])
    mysql.connection.commit()
    cur.close()
    flash("Tipo de Dispositivo Removido com Sucesso!")
    return redirect(url_for('listar_tipo_dispositivo'))



@app.route('/delete_localizacao/<id>')
def delete_localizacao(id):
    cur = mysql.connection.cursor()

    cur.execute("SELECT COUNT(*) FROM Dispositivo WHERE tipo_dispositivo = %s",[id])
    n = int(cur.fetchall()[0][0])
    if(n>0):
        flash("Não foi possivel eliminar Localizacao (está associado a pelo menos um Dispositivo)")
        return redirect(url_for('listar_localizacao'))

    cur.execute("SELECT COUNT(*) FROM Deslocacao WHERE localizacao_origem = %s OR localizacao_destino = %s",(id,id))
    n = int(cur.fetchall()[0][0])
    if(n>0):
        flash("Não foi possivel eliminar Localizacao (está associado a pelo menos uma Deslocacao)")
        return redirect(url_for('listar_localizacao'))

    cur.execute("DELETE FROM Localizacao WHERE id_Localizacao = %s",[id])
    mysql.connection.commit()
    cur.close()
    flash("Localizacao Removido com Sucesso!")
    return redirect(url_for('listar_localizacao'))



@app.route('/delete_dispositivo/<id>')
def delete_dispositivo(id):
    cur = mysql.connection.cursor()

    cur.execute("SELECT COUNT(*) FROM Deslocacao WHERE dispositivo = %s",[id])
    n = int(cur.fetchall()[0][0])
    if(n>0):
        flash("Não foi possivel eliminar Dispositivo (está associado a pelo menos uma Deslocacao)")
        return redirect(url_for('listar_dispositivo'))

    cur.execute("DELETE FROM Dispositivo WHERE id_Dispositivo = %s",[id])
    mysql.connection.commit()
    cur.close()
    flash("Dispositivo Removido com Sucesso!")
    return redirect(url_for('listar_dispositivo'))



@app.route('/delete_tipo_recurso_humano/<id>')
def delete_tipo_recurso_humano(id):
    cur = mysql.connection.cursor()

    cur.execute("SELECT COUNT(*) FROM Recurso_Humano WHERE tipo_recurso = %s",[id])
    n = int(cur.fetchall()[0][0])
    if(n>0):
        flash("Não foi possivel eliminar Tipo (está associado a pelo menos um Recurso Humano)")
        return redirect(url_for('listar_tipo_recurso_humano'))

    cur.execute("DELETE FROM Tipo_Recurso_Humano WHERE id_Tipo_Recurso_Humano = %s",[id])
    mysql.connection.commit()
    cur.close()
    flash("Tipo de Recurso Humano Removido com Sucesso!")
    return redirect(url_for('listar_tipo_recurso_humano'))




@app.route('/delete_especialidade/<id>')
def delete_especialidade(id):
    cur = mysql.connection.cursor()

    cur.execute("SELECT COUNT(*) FROM Recurso_Humano WHERE especialidade = %s",[id])
    n = int(cur.fetchall()[0][0])
    if(n>0):
        flash("Não foi possivel eliminar Especialidade (está associada a pelo menos um Recurso Humano)")
        return redirect(url_for('listar_especialidade'))

    cur.execute("DELETE FROM Especialidade WHERE id_Especialidade = %s",[id])
    mysql.connection.commit()
    cur.close()
    flash("Especialidade Removida com Sucesso!")
    return redirect(url_for('listar_especialidade'))




@app.route('/delete_recurso_humano/<id>')
def delete_recurso_humano(id):
    cur = mysql.connection.cursor()

    cur.execute("SELECT COUNT(*) FROM Deslocacao WHERE responsavel = %s",[id])
    n = int(cur.fetchall()[0][0])
    if(n>0):
        flash("Não foi possivel eliminar Recurso Humano (está associado a pelo menos uma Deslocação)")
        return redirect(url_for('listar_recurso_humano'))

    cur.execute("SELECT COUNT(*) FROM Recurso_Humano_manipula_Tipo_Dispositivo WHERE id_Recurso_Humano = %s",[id])
    n = int(cur.fetchall()[0][0])
    if(n>0):
        flash("Não foi possivel eliminar Recurso Humano (está associado a pelo menos uma Permissão)")
        return redirect(url_for('listar_recurso_humano'))

    cur.execute("DELETE FROM Recurso_Humano WHERE id_Recurso_Humano = %s",[id])
    mysql.connection.commit()
    cur.close()
    flash("Recurso Humano Removido com Sucesso!")
    return redirect(url_for('listar_recurso_humano'))




@app.route('/delete_deslocacao/<id>')
def delete_deslocacao(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM Deslocacao WHERE id_Deslocacao = %s",[id])
    mysql.connection.commit()
    cur.close()
    flash("Deslocação Removida com Sucesso!")
    return redirect(url_for('listar_deslocacao'))




@app.route('/delete_permissao/<id1>_<id2>')
def delete_permissao(id1,id2):
    cur = mysql.connection.cursor()
    
    cur.execute("""
        DELETE FROM Recurso_Humano_manipula_Tipo_Dispositivo
        WHERE (id_Recurso_Humano,id_Tipo_Dispositivo) = (%s,%s)
        """,(id1,id2))

    mysql.connection.commit()
    cur.close()
    flash("Permissão Removida com Sucesso!")
    return redirect(url_for('listar_permissoes'))
