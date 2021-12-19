from config import *

# [SQL] Drop da base de dados e Criação das Tabelas
@app.route('/reset_DB',methods=['POST'])
def reset_DB(auto_povoamento=True):
    if request.method == 'POST':
      
        print("\n\n\t[[ RESET DB 0]]\n\n")
        cur = mysql.connection.cursor()
        print("\n\t[[ RESET DB 1]]\n\n")
        cur.execute("DROP TABLE IF EXISTS Recurso_Humano_manipula_Tipo_Dispositivo")
        cur.execute("DROP TABLE IF EXISTS Deslocacao")
        cur.execute("DROP TABLE IF EXISTS Recurso_Humano")
        cur.execute("DROP TABLE IF EXISTS Especialidade")
        cur.execute("DROP TABLE IF EXISTS Tipo_Recurso_Humano")
        cur.execute("DROP TABLE IF EXISTS Dispositivo")
        cur.execute("DROP TABLE IF EXISTS Localizacao")
        cur.execute("DROP TABLE IF EXISTS Tipo_Dispositivo")
        
        cur.execute("""

            CREATE TABLE IF NOT EXISTS Tipo_Dispositivo (
              id_Tipo_Dispositivo INT NOT NULL AUTO_INCREMENT,
              descricao VARCHAR(45) NOT NULL,
              PRIMARY KEY (id_Tipo_Dispositivo))

            """)
        print("\n\t[[ RESET DB 2]]\n\n")

        cur.execute("""

            CREATE TABLE IF NOT EXISTS Localizacao (
              id_Localizacao INT NOT NULL AUTO_INCREMENT,
              descricao VARCHAR(45) NOT NULL,
              PRIMARY KEY (id_Localizacao))

            """)
        # print("\n\t[[ RESET DB 3]]\n\n")

        cur.execute("INSERT INTO Localizacao(id_Localizacao,descricao) VALUES (%s,%s)",[1,"Sala de Reparações"])


        cur.execute("""

            CREATE TABLE IF NOT EXISTS Dispositivo (
              id_Dispositivo INT NOT NULL AUTO_INCREMENT,
              estado VARCHAR(20) NOT NULL,
              estimativa_de_entrega INT NOT NULL,
              tipo_dispositivo INT NOT NULL,
              localizacao_atual INT NOT NULL,
              PRIMARY KEY (id_Dispositivo),
              CONSTRAINT fk_Dispositivo_Tipo_Dispositivo1
                FOREIGN KEY (tipo_dispositivo)
                REFERENCES Tipo_Dispositivo (id_Tipo_Dispositivo)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION,
              CONSTRAINT fk_Dispositivo_Localizacao1
                FOREIGN KEY (localizacao_atual)
                REFERENCES Localizacao (id_Localizacao)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION)

            """)

        cur.execute("""

            CREATE TABLE IF NOT EXISTS Tipo_Recurso_Humano (
              id_Tipo_Recurso_Humano INT NOT NULL AUTO_INCREMENT,
              descricao VARCHAR(45) NOT NULL,
              PRIMARY KEY (id_Tipo_Recurso_Humano))

            """)

        cur.execute("""

            CREATE TABLE IF NOT EXISTS Especialidade (
              id_Especialidade INT NOT NULL AUTO_INCREMENT,
              descricao VARCHAR(45) NOT NULL,
              PRIMARY KEY (id_Especialidade))

            """)

        cur.execute("""

            CREATE TABLE IF NOT EXISTS Recurso_Humano (
              id_Recurso_Humano INT NOT NULL AUTO_INCREMENT,
              nome VARCHAR(45) NOT NULL,
              data_nascimento DATE NOT NULL,
              tipo_recurso INT NOT NULL,
              especialidade INT NOT NULL,
              PRIMARY KEY (id_Recurso_Humano),
              CONSTRAINT fk_Recurso_Humano_Tipo_Recurso_Humano1
                FOREIGN KEY (tipo_recurso)
                REFERENCES Tipo_Recurso_Humano (id_Tipo_Recurso_Humano)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION,
              CONSTRAINT fk_Recurso_Humano_Especialidade1
                FOREIGN KEY (especialidade)
                REFERENCES Especialidade (id_Especialidade)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION)

            """)

        cur.execute("""

            CREATE TABLE IF NOT EXISTS Deslocacao (
              id_Deslocacao INT NOT NULL AUTO_INCREMENT,
              data DATE NOT NULL,
              dispositivo INT NOT NULL,
              responsavel INT NOT NULL,
              localizacao_origem INT NOT NULL,
              localizacao_destino INT NOT NULL,
              PRIMARY KEY (id_Deslocacao),
              CONSTRAINT fk_Deslocacao_Localizacao1
                FOREIGN KEY (localizacao_origem)
                REFERENCES Localizacao (id_Localizacao)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION,
              CONSTRAINT fk_Deslocacao_Localizacao2
                FOREIGN KEY (localizacao_destino)
                REFERENCES Localizacao (id_Localizacao)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION,
              CONSTRAINT fk_Deslocacao_Recurso_Humano1
                FOREIGN KEY (responsavel)
                REFERENCES Recurso_Humano (id_Recurso_Humano)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION,
              CONSTRAINT fk_Deslocacao_Dispositivo1
                FOREIGN KEY (dispositivo)
                REFERENCES Dispositivo (id_Dispositivo)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION)

            """)

        cur.execute("""

            CREATE TABLE IF NOT EXISTS Recurso_Humano_manipula_Tipo_Dispositivo (
              id_Recurso_Humano INT NOT NULL,
              id_Tipo_Dispositivo INT NOT NULL,
              PRIMARY KEY (id_Recurso_Humano, id_Tipo_Dispositivo),
              CONSTRAINT fk_Recurso_Humano_has_Tipo_Dispositivo_Recurso_Humano1
                FOREIGN KEY (id_Recurso_Humano)
                REFERENCES Recurso_Humano (id_Recurso_Humano)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION,
              CONSTRAINT fk_Recurso_Humano_has_Tipo_Dispositivo_Tipo_Dispositivo1
                FOREIGN KEY (id_Tipo_Dispositivo)
                REFERENCES Tipo_Dispositivo (id_Tipo_Dispositivo)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION)

            """)

        print("\n\n\t[[ RESET DB ]]\n\n")
        mysql.connection.commit()
        cur.close()
        flash("BD Resetada com Sucesso!")
        if auto_povoamento:
          povoamento()
        return redirect(url_for('index'))



def povoamento():
  print("\n\tPovoamento\n")
  cur = mysql.connection.cursor()

  cur.execute("""
    INSERT INTO Tipo_Dispositivo(descricao) VALUES
    ('Estetoscópio'),
    ('Bisturi'),
    ('Seringa'),
    ('Ventilador')
    """)

  cur.execute("""
    INSERT INTO Localizacao(descricao) VALUES
    ('Armazém'),
    ('Consultório A'),
    ('Consultório B'),
    ('Consultório C'),
    ('Internamento'),
    ('Enfermaria'),
    ('Bloco Operatório A'),
    ('Bloco Operatório B')
    """)

  cur.execute("""
    INSERT INTO Dispositivo(estado,estimativa_de_entrega,tipo_dispositivo,localizacao_atual) VALUES
    ('Funcional','0','1','3'),
    ('Funcional','0','2','7'),
    ('Funcional','0','1','4'),
    ('Não Funcional','0','3','7'),
    ('Em Reparação','5','3','1'),
    ('Funcional','0','1','2'),
    ('Funcional','0','4','7')
    """)

  cur.execute("""
    INSERT INTO Tipo_Recurso_Humano(descricao) VALUES
    ('Médico'),
    ('Enfermeiro')
    """)

  cur.execute("""
    INSERT INTO Especialidade(descricao) VALUES
    ('Medicina Geral'),
    ('Pneumologia'),
    ('Cardiologia'),
    ('Oncologia'),
    ('Enfermagem')
    """)

  cur.execute("""
    INSERT INTO Recurso_Humano(nome,data_nascimento,tipo_recurso,especialidade) VALUES
    ('José Carlos','1972-09-25','1','2'),
    ('Mario Esteves','1962-11-28','1','3'),
    ('Maria Mercedes','1982-03-14','2','5')
    """)

  cur.execute("""
    INSERT INTO Deslocacao(data,dispositivo,responsavel,localizacao_origem,localizacao_destino) VALUES
    ('2019-09-25','1','2','2','3'),
    ('2019-11-28','5','3','7','1')
    """)

  cur.execute("""
    INSERT INTO Recurso_Humano_manipula_Tipo_Dispositivo(id_Recurso_Humano,id_Tipo_Dispositivo) VALUES
    ('1','1'),
    ('3','3'),
    ('3','4'),
    ('2','1'),
    ('2','2')
    """)

  mysql.connection.commit()
  cur.close()
  flash("BD foi Repovoada com Sucesso!")