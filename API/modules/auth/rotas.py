from flask import Blueprint, request
from database import mysql

from modules.auth.validacao import login_validado, validate_user_id
from modules.auth.controllers import login_dir, login_pro, login_alu, todos_usuarios_dir, todos_usuarios_pro, todos_usuarios_alu, um_usuario_dir, um_usuario_pro, um_usuario_alu, professor_del, aluno_del, professor_up, aluno_up, professor_cre, aluno_cre

auth_rotas = Blueprint ('auth', __name__)

@auth_rotas.route('/login/diretor', methods=["POST"])
def login_diretor():
    # validacao dos dados de entrada
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
        'messagem':  'Bem-Vindo, login realizado com Sucesso!',
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
        'messagem': 'Bem-Vindo, login realizado com Sucesso!',
        'email': dados_recebido['email']
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
        'messagem': 'Bem-Vindo, login realizado com Sucesso!',
        'email': dados_recebido['email']
    }

@auth_rotas.route('/diretor', methods=["GET"])
def mostrar_usuarios_dir():

    all_dir = todos_usuarios_dir()
    return{
        'users_list' : all_dir
    }

@auth_rotas.route('/professor', methods=["GET"])
def mostrar_usuarios_pro():

    all_pro = todos_usuarios_pro()
    return{
        'users_list' : all_pro
    }

@auth_rotas.route('/aluno', methods=["GET"])
def mostrar_usuarios_alu():

    all_alu = todos_usuarios_alu()
    return{
        'users_list' : all_alu
    }

@auth_rotas.route('/usuario/diretor', methods=["GET"])
def mostrar_usuario_dir():
    dados_recebidos = request.args
    msg, status = validate_user_id (dados_recebidos)
    if not status :
        return msg, 400
    
    one_dir = um_usuario_dir(dados_recebidos['id'])
    return{
        'users_list' : one_dir
    }

@auth_rotas.route('/usuario/professor', methods=["GET"])
def mostrar_usuario_pro():
    dados_recebidos = request.args
    msg, status = validate_user_id (dados_recebidos)
    if not status :
        return msg, 400
    
    one_pro = um_usuario_pro(dados_recebidos['id'])
    return{
        'users_list' : one_pro
    }

@auth_rotas.route('/usuario/aluno', methods=["GET"])
def mostrar_usuario_alu():
    dados_recebidos = request.args
    msg, status = validate_user_id (dados_recebidos)
    if not status :
        return msg, 400
    
    one_alu = um_usuario_alu(dados_recebidos['id'])
    return{
        'users_list' : one_alu
    }

@auth_rotas.route('/professor', methods=["DELETE"])
def professor_delete():
    dados_recebido = request.args
    msg, status = validate_user_id(dados_recebido)
    if not status:
        return msg, 400

    message, status = professor_del(dados_recebido['id'])
    return message, status

@auth_rotas.route('/aluno', methods=["DELETE"])
def aluno_delete():
    dados_recebido = request.args
    msg, status = validate_user_id(dados_recebido)
    if not status:
        return msg, 400

    message, status = aluno_del(dados_recebido['id'])
    return message, status

@auth_rotas.route('/professor', methods=["PUT"])
def professor_update():
    dados_recebido_url = request.args
    msg, status = validate_user_id(dados_recebido_url)
    if not status:
        return msg, 400
    
    dados_recebidos_corpo = request.json 
    msg, status = professor_up(dados_recebido_url['id'], dados_recebidos_corpo)

    return msg, status 

@auth_rotas.route('/aluno', methods=["PUT"])
def aluno_update():
    dados_recebido_url = request.args
    msg, status = validate_user_id(dados_recebido_url)
    if not status:
        return msg, 400
    
    dados_recebidos_corpo = request.json 
    msg, status  = aluno_up (dados_recebido_url['id'], dados_recebidos_corpo)

    return msg, status

@auth_rotas.route('/professor', methods=["POST"])
def criar_professor():
    dados_recebidos_url = request.args
    msg, status = validate_user_id(dados_recebidos_url)
    if not status:
        return msg, 400

    dados_recebidos_corpo = request.json 
    new_users = professor_cre (dados_recebidos_url['id'], dados_recebidos_corpo)
    
    return{
        'new_users_list': new_users
    }

@auth_rotas.route('/aluno', methods=["POST"])
def criar_aluno():
    dados_recebidos_url = request.args
    msg, status = validate_user_id(dados_recebidos_url)
    if not status:
        return msg, 400

    dados_recebidos_corpo = request.json 
    new_users = aluno_cre (dados_recebidos_url['id'], dados_recebidos_corpo)
    
    return{
        'new_users_list': new_users
    }