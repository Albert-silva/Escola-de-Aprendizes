from flask import Blueprint, request

from modules.auth.validacao import login_validado, validate_user_id
from modules.auth.controllers import login_dir, login_pro, login_alu, todos_usuarios, um_usuario, professor_del, aluno_del, professor_up, aluno_up, create_professor, create_aluno

auth_rotas = Blueprint ('auth', __name__)

@auth_rotas.route('/login/diretor', methods=["POST"])
def login_diretor():
    dados_recebido = request.json
    msg, status = login_validado(request.json)
    if not status:
        return msg, 400

    # processamento
    msg, status = login_dir(dados_recebido)
    if status >= 400:
        return msg, status

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
    msg, status = login_pro(dados_recebido)
    if status >= 400:
        return msg, status
    
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
    msg, status = login_alu(dados_recebido)
    if status >= 400:
        return msg, status
    
    # formatamos o retorno
    return {
        'mensagem': 'Bem-Vindo, login realizado com Sucesso!',
        'email': dados_recebido['Email']
    }

@auth_rotas.route('/usuarios', methods=["GET"])
def mostrar_usuarios():
    new_users = todos_usuarios()
    return{
        'users_list' : new_users
    }

@auth_rotas.route('/usuario', methods=["GET"])
def mostrar_usuario():
    dados_recebidos = request.args
    msg, status = validate_user_id (dados_recebidos)
    if not status :
        return msg, 400
    
    user = um_usuario(dados_recebidos['id'])
    if not user:
        return 'Usuário não encontrado!', 404

    return user

@auth_rotas.route('/professor', methods=["DELETE"])
def professor_delete():
    dados_recebido = request.args
    msg, status = validate_user_id(dados_recebido)
    if not status:
        return msg, 400

    new_users = professor_del (dados_recebido['id'])
    return {
        'new_users_list': new_users
    }

@auth_rotas.route('/aluno', methods=["DELETE"])
def aluno_delete():
    dados_recebido = request.args
    msg, status = validate_user_id(dados_recebido)
    if not status:
        return msg, 400

    new_users = aluno_del (dados_recebido['id'])
    return {
        'new_users_list': new_users
    }

@auth_rotas.route('/professor', methods=["PUT"])
def professor_update():
    dados_recebido_url = request.args
    msg, status = validate_user_id(dados_recebido_url)
    if not status:
        return msg, 400
    
    dados_recebidos_corpo = request.json 
    new_users = professor_up (dados_recebido_url['id'], dados_recebidos_corpo)

    return {
        'new_users_list': new_users
    }

@auth_rotas.route('/aluno', methods=["PUT"])
def aluno_update():
    dados_recebido_url = request.args
    msg, status = validate_user_id(dados_recebido_url)
    if not status:
        return msg, 400
    
    dados_recebidos_corpo = request.json 
    new_users = aluno_up (dados_recebido_url['id'], dados_recebidos_corpo)

    return {
        'new_users_list': new_users
    }

@auth_rotas.route('/professor', methods=["POST"])
def criar_professor():
    dados_recebidos_url = request.json
    msg, status = validate_user_id(dados_recebidos_url)
    if not status:
        return msg, 400

    dados_recebidos_corpo = request. json 
    new_users = create_professor (dados_recebidos_corpo)
    
    return{
        'new_users_list': new_users
    }

@auth_rotas.route('/aluno', methods=["POST"])
def criar_aluno():
    dados_recebidos_url = request.json
    msg, status = validate_user_id(dados_recebidos_url)
    if not status:
        return msg, 400

    dados_recebidos_corpo = request. json 
    new_users = create_aluno (dados_recebidos_corpo)
    
    return{
        'new_users_list': new_users
    }