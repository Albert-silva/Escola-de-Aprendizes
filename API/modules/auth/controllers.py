import jwt
import pytz
from datetime import datetime, timedelta
from flask import request

from database import mysql

def login_dir(dados_recebido):
    cursor = mysql.get_db().cursor()

    cursor.execute("SELECT * FROM Diretor WHERE Email = %s", [dados_recebido['email']])
    usuario_selecionado = cursor.fetchone()

    if not usuario_selecionado:
        return 'Usuário não encontrado', 404

    if usuario_selecionado[6] != dados_recebido['senha']:
        return 'Senha Incorreta', 403
    
    data_hora_atual = datetime.now(tz=pytz.timezone('America/Sao_Paulo'))
    dados = {
        'nome': usuario_selecionado[0],
        'id': usuario_selecionado[3],
        'iat': data_hora_atual,
        'exp': data_hora_atual + timedelta(hours=8000),
        'tipo': 'Diretor'
    }
    token = jwt.encode(dados, "SENHA_TOKEN", algorithm="HS256")

    cursor.close()

    return token, 200

def login_pro(dados_recebido):
    cursor = mysql.get_db().cursor()

    cursor.execute("SELECT * FROM Professores WHERE email = %s", [dados_recebido['email']])
    usuario_selecionado = cursor.fetchone()

    if not usuario_selecionado:
        return 'Usuário não encontrado', 404

    if usuario_selecionado[6] != dados_recebido['senha']:
        return 'Senha Incorreta', 403

    data_hora_atual = datetime.now(tz=pytz.timezone('America/Sao_Paulo'))
    dados = {
        'nome': usuario_selecionado[0],
        'id': usuario_selecionado[3],
        'iat': data_hora_atual,
        'exp': data_hora_atual + timedelta(hours=8000),
        'tipo': 'Professores'
    }
    token = jwt.encode(dados, "SENHA_TOKEN", algorithm="HS256")

    cursor.close()

    return token, 200

def login_alu(dados_recebido):
    cursor = mysql.get_db().cursor()

    cursor.execute("SELECT * FROM Alunos WHERE email = %s", [dados_recebido['email']])
    usuario_selecionado = cursor.fetchone()

    if not usuario_selecionado:
        return 'Usuário não encontrado', 404

    if usuario_selecionado[5] != dados_recebido['senha']:
        return 'Senha Incorreta', 403
    
    data_hora_atual = datetime.now(tz=pytz.timezone('America/Sao_Paulo'))
    dados = {
        'nome': usuario_selecionado[0],
        'id': usuario_selecionado[2],
        'iat': data_hora_atual,
        'exp': data_hora_atual + timedelta(hours=8000),
        'tipo': 'Alunos'
    }
    token = jwt.encode(dados, "SENHA_TOKEN", algorithm="HS256")

    cursor.close()

    return token, 200

def todos_usuarios_dir ():
    cursor = mysql.get_db().cursor()

    cursor.execute("SELECT * FROM Diretor")

    users_db = cursor.fetchall()

    all_users = []

    for user in users_db:
        new_user = {
            'Nome': user[0],
            'cpf': user[1],
            'E-mail': user[2],
            'id': user[3],
            'Createdat': user[4],
            'Edictedat': user[5]

        }

        all_users.append(new_user)

    cursor.close()

    return all_users

def todos_usuarios_pro ():
    cursor = mysql.get_db().cursor()

    cursor.execute("SELECT * FROM Professores")

    users_db = cursor.fetchall()

    all_users = []

    for user in users_db:
        new_user = {
            'Nome': user[0],
            'cpf': user[1],
            'E-mail': user[2],
            'id': user[3],
            'Createdat': user[4],
            'Edictedat': user[5]

        }

        all_users.append(new_user)

    cursor.close()

    return all_users

def todos_usuarios_alu ():
    cursor = mysql.get_db().cursor()

    cursor.execute("SELECT * FROM Alunos")

    users_db = cursor.fetchall()

    all_users = []

    for user in users_db:
        new_user = {
            'Nome': user[0],
            'E-mail': user[1],
            'id': user[2],
            'Createdat': user[3],
            'Edictedat': user[4]

        }

        all_users.append(new_user)

    cursor.close()

    return all_users

def um_usuario_dir (id):
    cursor = mysql.get_db().cursor()

    cursor.execute("SELECT * FROM Diretor WHERE id = %s", [id])

    user_db = cursor.fetchone()

    if user_db :
        user = {
            'Nome': user_db[0],
            'cpf': user_db[1],
            'E-mail': user_db[2],
            'id': user_db[3],
            'Createdat': user_db[4],
            'Edictedat': user_db[5]

        }
        return user
    cursor.close()

    return None

def um_usuario_pro (id):
    cursor = mysql.get_db().cursor()

    cursor.execute("SELECT * FROM Professores WHERE id = %s", [id])

    user_db = cursor.fetchone()

    if user_db :
        user = {
            'Nome': user_db[0],
            'cpf': user_db[1],
            'E-mail': user_db[2],
            'id': user_db[3],
            'Createdat': user_db[4],
            'Edictedat': user_db[5]

        }
        return user
    cursor.close()

    return None

def um_usuario_alu (id):
    cursor = mysql.get_db().cursor()

    cursor.execute("SELECT * FROM Alunos WHERE id = %s", [id])

    user_db = cursor.fetchone()

    if user_db :
        user = {
            'Nome': user_db[0],
            'E-mail': user_db[1],
            'id': user_db[2],
            'Createdat': user_db[3],
            'Edictedat': user_db[4]

        }
        return user
    cursor.close()

    return None

def professor_del (id):
    cursor = mysql.get_db().cursor()

    # verificar se existe o usuario com o ID X no banco
    cursor.execute("SELECT * FROM Professores WHERE id = %s", [id])
    usuario_selecionado = cursor.fetchone()

    if not usuario_selecionado:
        return 'Usuário não encontrado', 404
    
    cursor.execute("DELETE FROM Professores WHERE id = %s", [id])

    mysql.get_db().commit()

    cursor.close()
    
    return 'Usuário deletado com sucesso!', 200

def aluno_del (id):
    cursor = mysql.get_db().cursor()

    # verificar se existe o usuario com o ID X no banco
    cursor.execute("SELECT * FROM Alunos WHERE id = %s", [id])
    usuario_selecionado = cursor.fetchone()

    if not usuario_selecionado:
        return 'Usuário não encontrado', 404
    
    cursor.execute("DELETE FROM Alunos WHERE id = %s", [id])

    mysql.get_db().commit()

    cursor.close()
    
    return 'Usuário deletado com sucesso!', 200

def professor_up (id, user_infos):
    cursor = mysql.get_db().cursor()

    # verificar se existe o usuario com o ID X no banco
    cursor.execute("SELECT * FROM Professores WHERE id = %s", [id])
    usuario_selecionado = cursor.fetchone()

    if not usuario_selecionado:
        return 'Usuário não encontrado', 404

    # organizar as novas informacoes
    novo_nome = user_infos['nome']
    novo_email = user_infos['email']
    novo_cpf = user_infos['cpf']
    data_atual = datetime.now()

    # atualizar no banco de dados com as novas informacoes para o usuario
    cursor.execute("UPDATE Professores SET nome = %s, email = %s, cpf = %s, edictedat = %s WHERE id = %s", 
        [novo_nome, novo_email, novo_cpf, data_atual, id])

    mysql.get_db().commit()

    cursor.close()

    return 'Usuário atualizado com sucesso!', 200

def aluno_up (id, user_infos):
    cursor = mysql.get_db().cursor()

    # verificar se existe o usuario com o ID X no banco
    cursor.execute("SELECT * FROM Alunos WHERE id = %s", [id])
    usuario_selecionado = cursor.fetchone()

    if not usuario_selecionado:
        return 'Usuário não encontrado', 404

    # organizar as novas informacoes
    novo_nome = user_infos['nome']
    novo_email = user_infos['email']
    data_atual = datetime.now()

    # atualizar no banco de dados com as novas informacoes para o usuario
    cursor.execute("UPDATE Alunos SET nome = %s, email = %s, edictedat = %s WHERE id = %s", 
        [novo_nome, novo_email, data_atual, id])

    mysql.get_db().commit()

    cursor.close()

    return 'Usuário atualizado com sucesso!', 200

def professor_cre(id, user_infos):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM Professores where id = %s", [id])
    usuario_selecionado = cursor.fetchone()

    if usuario_selecionado:
        return 'Usuário já existe', 404
    
    nome  = user_infos['nome']
    cpf = user_infos['cpf']
    email = user_infos['email']
    senha = user_infos['senha']
    data = datetime.now()

    cursor.execute("INSERT INTO Professores (nome , cpf , email , senha , createdeat) VALUES (%s, %s, %s, %s, %s)",
    [nome, cpf, email, senha, data])

    mysql.get_db().commit()

    cursor.close()

    return 'Professor cadastrado com sucesso', 200

def aluno_cre(id, user_infos):

    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM Alunos where id = %s", [id])
    usuario_selecionado = cursor.fetchone()

    if usuario_selecionado:
        return 'Usuário não existe', 404
    
    nome  = user_infos['nome']
    email = user_infos['email']
    senha = user_infos['senha']
    data = datetime.now()

    cursor.execute("INSERT INTO Alunos (nome, email , senha , createdeat) VALUES (%s, %s, %s, %s)",
    [nome, email, senha, data])

    mysql.get_db().commit()

    cursor.close()

    return 'Aluno cadastrado com sucesso', 200