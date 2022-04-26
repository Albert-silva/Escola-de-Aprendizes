from datetime import datetime
from flask import Blueprint, request

from modules.auth.validacao import login_validado, validate_user_id

auth_rotas = Blueprint ('auth', __name__)

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

@auth_rotas.route('/login/diretor', methods=["POST"])
def login_diretor():
    dados_recebido = request.json
    msg, status = login_validado(request.json)
    if not status:
        return msg, 400

    # processamento
    usuario_selecionado = None
    for user in Diretores:
        if user['Email'] == dados_recebido['email']:
            usuario_selecionado = user
            break

    if not usuario_selecionado:
        return 'Usuário não encontrado', 404

    if user['senha'] != dados_recebido['senha']:
        return 'Senha Incorreta', 403
    
    # formatamos o retorno
    return {
        'mensagem': 'Bem-Vindo, login realizado com Sucesso!',
        'email': dados_recebido['email']
    }
    
@auth_rotas.route('/login/professor', methods=["POST"])
def login_professor():
    dados_recebido = request.json
    msg, status = login_validado(request.json)
    if not status:
        return msg, 400

    # processamento
    usuario_selecionado = None
    for user in Professores:
        if user['Email'] == dados_recebido['Email']:
            usuario_selecionado = user
            break

    if not usuario_selecionado:
        return 'Usuário não encontrado', 404

    if user['senha'] != dados_recebido['senha']:
        return 'Senha Incorreta', 403
    
    # formatamos o retorno
    return {
        'mensagem': 'Bem-Vindo, login realizado com Sucesso!',
        'email': dados_recebido['E-mail']
    }

@auth_rotas.route('/login/aluno', methods=["POST"])
def login_aluno():
    dados_recebido = request.json
    msg, status = login_validado(request.json)
    if not status:
        return msg, 400

    # processamento
    usuario_selecionado = None
    for user in Alunos:
        if user['Email'] == dados_recebido['Email']:
            usuario_selecionado = user
            break

    if not usuario_selecionado:
        return 'Usuário não encontrado', 404

    if user['senha'] != dados_recebido['senha']:
        return 'Senha Incorreta', 403
    
    # formatamos o retorno
    return {
        'mensagem': 'Bem-Vindo, login realizado com Sucesso!',
        'email': dados_recebido['Email']
    }

@auth_rotas.route('/usuarios', methods=["GET"])
def mostrar_usuarios():
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

@auth_rotas.route('/usuario', methods=["GET"])
def mostrar_usuario():
    dados_recebidos = request.args
    msg, status = validate_user_id (dados_recebidos)
    if not status :
        return msg, 400
   
    for user in Diretores:
        if int(dados_recebidos['id']) == user['id']:
            del user['senha']
            return user
    
    for user in Professores:
        if int(dados_recebidos['id']) == user['id']:
            del user['senha']
            return user
    
    for user in Alunos:
        if int(dados_recebidos['id']) == user['id']:
            del user['senha']
            return user

    return 'Usuário não encontrado!', 404


@auth_rotas.route('/usuario', methods=["DELETE"])
def user_deleted():
    dados_recebido = request.args
    msg, status = validate_user_id(dados_recebido)
    if not status:
        return msg, 400

    new_users = []
    for user in Professores:
        if user['id'] != int(dados_recebido['id']):
            new_users.append(user)
    
    for user in Alunos:
        if user['id'] != int(dados_recebido['id']):
            new_users.append(user)

    return {
        'new_users_list': new_users
    }

@auth_rotas.route('/usario', methods=["PUT"])
def user_update():
    dados_recebido_url = request.args
    msg, status = validate_user_id(dados_recebido_url)
    if not status:
        return msg, 400

    dados_recebido_corpo = request.json

    new_users = []
    for user in Professores:
        if int(dados_recebido_url['id']) == user['id']:
            if 'nome' in dados_recebido_corpo:
                user['name'] = dados_recebido_corpo['nome']

            if 'email' in dados_recebido_corpo:
                user['email'] = dados_recebido_corpo['email']
        new_users.append(user)

    for user in Alunos:
        if int(dados_recebido_url['id']) == user['id']:
            if 'nome' in dados_recebido_corpo:
                user['name'] = dados_recebido_corpo['nome']

            if 'email' in dados_recebido_corpo:
                user['email'] = dados_recebido_corpo['email']
        new_users.append(user)

    return {
        'new_users_list': new_users
    }

@auth_rotas.route('/usuario', methods=["POST"])
def criar_usuario():
    dados_recebidos_corpo = request.args

    new_users = []
    for dados_recebidos_corpo in Professores:
        if dados_recebidos_corpo ['cpf'] != Professores['cpf']:
            Professores['cpf'] = dados_recebidos_corpo['cpf']
       
        if dados_recebidos_corpo ['email'] != Professores['Email']:
            Professores['Email'] = dados_recebidos_corpo['cpf']
       
        if dados_recebidos_corpo ['nome'] != Professores['nome']:
            Professores['nome'] = dados_recebidos_corpo['nome']
    new_users.append(Professores)

    for dados_recebidos_corpo in Alunos:
        if dados_recebidos_corpo ['cpf'] != Alunos['cpf']:
            Alunos['cpf'] = dados_recebidos_corpo['cpf']
       
        if dados_recebidos_corpo ['email'] != Alunos['Email']:
            Alunos['Email'] = dados_recebidos_corpo['cpf']
       
        if dados_recebidos_corpo ['nome'] != Alunos['nome']:
            Alunos['nome'] = dados_recebidos_corpo['nome']
    new_users.append(Alunos)
   
    return{
        'new_users_list': new_users
    }