from datetime import datetime
from flask import request

Diretores = [
    {
        'Nome': 'Beto',
        'cpf': 12345678910,
        'id': 1,
        'Email': 'carlosnoronha@eaprendizes.com',
        'senha': 741852,
        'created_at': datetime(2022, 5, 1, 12, 0),
        'updated_at': datetime(2022, 5, 1, 12, 0),
     }
]
Professores = [ 
    {
        'Nome': 'Marcos',
        'cpf': 98765432109,
        'id': 2,
        'Email': 'marcoshefa@eaprendizes.com',
        'senha': 963852,
        'created_at': datetime(2022, 5, 1, 12, 0),
        'updated_at': datetime(2022, 5, 1, 12, 0),
     }
]
Alunos = [
    { 
        'Nome': 'Albert',
        'Email': 'albert@eaprendizes.com',
        'id': 3,
        'senha': 852741,
        'created_at': datetime(2022, 5, 1, 12, 0),
        'updated_at': datetime(2022, 5, 1, 12, 0),
     }
]

def login_dir(dados_recebido):
    usuario_selecionado = None
    for user in Diretores:
        if user['Email'] == dados_recebido['email']:
            usuario_selecionado = user
            break

    if not usuario_selecionado:
        return 'Usuário não encontrado', 404

    if user['senha'] != dados_recebido['senha']:
        return 'Senha Incorreta', 403
    return '', 200

def login_pro(dados_recebido):
    usuario_selecionado = None
    for user in Professores:
        if user['Email'] == dados_recebido['Email']:
            usuario_selecionado = user
            break

    if not usuario_selecionado:
        return 'Usuário não encontrado', 404

    if user['senha'] != dados_recebido['senha']:
        return 'Senha Incorreta', 403
    return '', 200

def login_alu(dados_recebido):
    usuario_selecionado = None
    for user in Alunos:
        if user['Email'] == dados_recebido['Email']:
            usuario_selecionado = user
            break

    if not usuario_selecionado:
        return 'Usuário não encontrado', 404

    if user['senha'] != dados_recebido['senha']:
        return 'Senha Incorreta', 403
    return '', 200

def todos_usuarios ():
    dados_recebidos = request.args
    if 'tipo' in dados_recebidos:
        if dados_recebidos ['tipo'] == 'Professores':
            return {
                'Professores': Professores
            }
        if dados_recebidos ['tipo'] == 'Diretores':
            return {
                'Diretores': Diretores
            }
        if dados_recebidos ['tipo'] == 'Alunos':
            return {
                'Alunos': Alunos
            }
    return {
        'Diretores': Diretores,
        'Professores': Professores,
        'Alunos': Alunos
    }

def um_usuario (id):
    for user in Diretores:
        if int(id) == user['id']:
            del user['senha']
            return user
    
    for user in Professores:
        if int(id) == user['id']:
            del user['senha']
            return user
    
    for user in Alunos:
        if int(id) == user['id']:
            del user['senha']
            return user

    return None 

def professor_del (id):
    new_users = []
    for user in Professores:
        if user['id'] != int(id):
            new_users.append(user)
    return new_users

def aluno_del (id):
    new_users = []
    for user in Alunos:
        if user['id'] != int(id):
            new_users.append(user)
    return new_users

def professor_up (id, user_infos):
    new_users = []
    for user in Professores:
        if int(id) == user['id']:
            if 'nome' in user_infos:
                user['name'] = user_infos['nome']

            if 'email' in user_infos:
                user['email'] = user_infos['email']
        new_users.append(user)
    return new_users

def aluno_up (id, user_infos):
    new_users = []
    for user in Alunos:
        if int(id) == user['id']:
            if 'nome' in user_infos:
                user['name'] = user_infos['nome']

            if 'email' in user_infos:
                user['email'] = user_infos['email']
        new_users.append(user)
    return new_users

def professor_cre(id, user_infos):

    new_users = []
    for user in Professores:
        if int(id) == user['id']:
            if  'Email' in user_infos:
                return 'Professor já existe!', 409
    new_users.append()
    
    return new_users

def aluno_cre(id, user_infos):

    new_users = []
    for user in Alunos:
        if int(id) == user ['id']:
            if 'Email' in user_infos:
                return 'Aluno já existe!', 409
    new_users.append()
    
    return new_users