from database import mysql

def lista_conteudos():
    cursor = mysql.get_db().cursor()

    cursor.execute("SELECT * FROM Conteudo INNER JOIN Professores on Conteudo.id_professor = Professores.id")

    conteudos_db = cursor.fetchall()

    all_conteudos = []

    for conteudo in conteudos_db:
        new_conteudo = {
            'id': conteudo[0],
            'nome': conteudo[1],
            'descricao': conteudo[2],
            'nome_professor': conteudo[4]
        }

        all_conteudos.append(new_conteudo)

    cursor.close()

    return all_conteudos

def seleciona_conteudo(id):
    cursor = mysql.get_db().cursor()

    cursor.execute("SELECT * FROM Conteudo INNER JOIN Professores on Conteudo.id_professor = Professores.id WHERE Conteudo.id = %s", [id])
    conteudo = cursor.fetchone()
    if not conteudo:
        return 'Conteudo não encontrado', 404

    conteudo_formated = {
        'id': conteudo[0],
        'nome': conteudo[1],
        'descricao': conteudo[2],
        'nome_professor': conteudo[4]
    }

    cursor.close()

    return conteudo_formated, 200

def deleta_conteudo (id):
    cursor = mysql.get_db().cursor()

    cursor.execute("SELECT * FROM Conteudo WHERE id = %s", [id])
    conteudo = cursor.fetchone()
    if not conteudo:
        return 'Conteudo não encontrada', 404
    
    cursor.execute("DELETE FROM Conteudo WHERE id = %s", [id])

    mysql.get_db().commit()

    cursor.close()
    
    return 'Conteudo deletado com sucesso!', 200

def cria_conteudo(dados_conteudo):
    cursor = mysql.get_db().cursor()

    nome = dados_conteudo['nome']
    descricao = dados_conteudo.get('descricao', '')
    id_professor = dados_conteudo['id_professor']

    cursor.execute("SELECT * FROM Conteudo WHERE nome = %s", [nome])
    conteudo = cursor.fetchone()
    if conteudo:
        return 'Conteudo já existe no banco de dados', 409

    cursor.execute("INSERT INTO Conteudo (nome, descricao, id_professor) VALUES (%s, %s, %s, %s)", 
        [nome, descricao, id_professor])

    mysql.get_db().commit()

    cursor.close()

    return 'Conteudo cadastrado com sucesso', 201

def atualiza_conteudo(id, novos_dados):
    cursor = mysql.get_db().cursor()

    cursor.execute("SELECT * FROM Conteudo WHERE id = %s", [id])
    conteudo = cursor.fetchone()
    if not conteudo:
        return 'Conteudo não encontrado', 404

    nome_conteudo = conteudo[1]
    descricao_conteudo = conteudo[2]

    if 'nome' in novos_dados and len(novos_dados['nome']) > 0:
        nome_conteudo = novos_dados['nome']

    if 'descricao' in novos_dados and len(novos_dados['descricao']) > 0:
        descricao_conteudo = novos_dados['descricao']

    
    cursor.execute("UPDATE Conteudo SET nome = %s, descricao = %s WHERE id = %s", 
        [nome_conteudo, descricao_conteudo, id])

    mysql.get_db().commit()

    cursor.close()

    return 'Conteudo atualizado com sucesso!', 200

def aluno_conteudo(id_conteudo):
    '''Seleciona os alunos de um conteudo especifico'''
    cursor = mysql.get_db().cursor()

    cursor.execute("SELECT * FROM Aluno_conteudo INNER JOIN Conteudo ON Aluno_conteudo.id_conteudo = Conteudo.id INNER JOIN Alunos on Aluno_conteudo.id_aluno = Alunos.id WHERE id_conteudo = %s", [id_conteudo])

    conteudo_db = cursor.fetchall()
    all_conteudos = []

    for conteudo in conteudo_db:
        new_conteudo = {
            'Nome Conteudo': conteudo[3],
            'Nome Aluno': conteudo[6]

        }

        all_conteudos.append(new_conteudo)

    cursor.close()


    return all_conteudos

def conteudo_aluno(id_aluno):
    '''Seleciona os conteudos de um aluno especifico'''
    cursor = mysql.get_db().cursor()

    cursor.execute("SELECT * FROM Aluno_conteudo INNER JOIN Conteudo ON Aluno_conteudo.id_conteudo= Conteudo.id INNER JOIN Alunos on Aluno_conteudo.id_aluno = Alunos.id WHERE id_aluno = %s", [id_aluno])

    aluno_db = cursor.fetchall()
    all_alunos = []

    for aluno in aluno_db:
        new_aluno = {
            'Nome Conteudo': aluno[3],
            'Nome Aluno': aluno[6]

        }

        all_alunos.append(new_aluno)

    cursor.close()


    return all_alunos, 200

def cria_aluno_conteudo (dados_recebidos):
    '''Cria a conexão entre aluno e conteudo'''
    cursor = mysql.get_db().cursor()

    id_conteudo = dados_recebidos['id_conteudo']
    id_aluno = dados_recebidos['id_aluno']

    try:
        cursor.execute("INSERT INTO Aluno_conteudo (id_conteudo, id_aluno) VALUES (%s, %s)", 
        [id_conteudo, id_aluno])

        mysql.get_db().commit()
    except:
        
        return 'Revise os dados enviados', 404

    cursor.close()

    return 'Aluno adicionado a conteudo com sucesso', 201