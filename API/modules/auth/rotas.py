from flask import Blueprint, request
from database import mysql

from decorators import validate_token
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
        'email': dados_recebido['email'],
        'token': msg
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
        'email': dados_recebido['email'],
        'token': msg
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
        'email': dados_recebido['email'],
        'token': msg
    }

@auth_rotas.route('/diretor', methods=["GET"])
@validate_token
def mostrar_usuarios_dir():
    dados_usuarios = request.user
    if dados_usuarios ['tipo'] != 'Diretor':
        return 'Usuário não autorizado!', 403

    all_dir = todos_usuarios_dir()
    return{
        'users_list' : all_dir
    }

@auth_rotas.route('/professor', methods=["GET"])
@validate_token
def mostrar_usuarios_pro():
    dados_usuarios = request.user
    if dados_usuarios ['tipo'] != 'Diretor':
        return 'Usuário não autorizado!', 403

    all_pro = todos_usuarios_pro()
    return{
        'users_list' : all_pro
    }

@auth_rotas.route('/aluno', methods=["GET"])
@validate_token
def mostrar_usuarios_alu():
    dados_usuarios = request.user
    if dados_usuarios ['tipo'] != 'Diretor' and dados_usuarios ['tipo'] != 'Professores':
        return 'Usuário não autorizado!', 403

    all_alu = todos_usuarios_alu()
    return{
        'users_list' : all_alu
    }

@auth_rotas.route('/usuario/diretor', methods=["GET"])
@validate_token
def mostrar_usuario_dir():
    dados_recebidos = request.args
    dados_usuarios = request.user
    if dados_usuarios ['tipo'] != 'Diretor':
        return 'Usuário não autorizado!', 403

    msg, status = validate_user_id (dados_recebidos)
    if not status :
        return msg, 400
    
    one_dir = um_usuario_dir(dados_recebidos['id'])
    return{
        'users_list' : one_dir
    }

@auth_rotas.route('/usuario/professor', methods=["GET"])
@validate_token
def mostrar_usuario_pro():
    dados_recebidos = request.args
    dados_usuarios = request.user
    if dados_usuarios ['tipo'] != 'Diretor' or dados_usuarios ['tipo'] == 'Alunos' or (dados_usuarios ['tipo'] == 'Professores' or dados_usuarios['id'] != int (dados_recebidos['id'])):
        return 'Usuário não autorizado!', 403

    msg, status = validate_user_id (dados_recebidos)
    if not status :
        return msg, 400
    
    one_pro = um_usuario_pro(dados_recebidos['id'])
    return one_pro

@auth_rotas.route('/usuario/aluno', methods=["GET"])
@validate_token
def mostrar_usuario_alu():
    dados_recebidos = request.args
    dados_usuarios = request.user
    if dados_usuarios ['tipo'] != 'Diretor' or dados_usuarios ['tipo'] == 'Professores' or (dados_usuarios ['tipo'] == 'Alunos' and dados_usuarios['id'] != int (dados_recebidos['id'])):
        return 'Usuário não autorizado!', 403

    msg, status = validate_user_id (dados_recebidos)
    if not status :
        return msg, 400
    
    one_alu = um_usuario_alu(dados_recebidos['id'])
    return{
        'users_list' : one_alu
    }

@auth_rotas.route('/professor', methods=["DELETE"])
@validate_token
def professor_delete():
    dados_recebido = request.args
    dados_usuarios = request.user
    if dados_usuarios ['tipo'] != 'Diretor' or (dados_usuarios ['tipo'] == 'Professores' or dados_usuarios['id'] != int (dados_recebido['id'])):
        return 'Usuário não autorizado!', 403

    msg, status = validate_user_id(dados_recebido)
    if not status:
        return msg, 400

    message, status = professor_del(dados_recebido['id'])
    return message, status

@auth_rotas.route('/aluno', methods=["DELETE"])
@validate_token
def aluno_delete():
    dados_recebido = request.args
    dados_usuarios = request.user
    if dados_usuarios ['tipo'] != 'Diretor' and dados_usuarios ['tipo'] != 'Professores':
        return 'Usuário não autorizado!', 403

    msg, status = validate_user_id(dados_recebido)
    if not status:
        return msg, 400

    message, status = aluno_del(dados_recebido['id'])
    return message, status

@auth_rotas.route('/professor', methods=["PUT"])
@validate_token
def professor_update():
    dados_recebido_url = request.args
    dados_usuarios = request.user
    if dados_usuarios ['tipo'] != 'Diretor' and dados_usuarios ['tipo'] == 'Alunos' or (dados_usuarios ['tipo'] == 'Professores' and dados_usuarios['id'] != int (dados_recebido_url['id'])):
        return 'Usuário não autorizado!', 403

    msg, status = validate_user_id(dados_recebido_url)
    if not status:
        return msg, 400
    
    dados_recebidos_corpo = request.json 
    msg, status = professor_up(dados_recebido_url['id'], dados_recebidos_corpo)

    return msg, status 

@auth_rotas.route('/aluno', methods=["PUT"])
@validate_token
def aluno_update():
    dados_recebido_url = request.args
    dados_usuarios = request.user
    if dados_usuarios ['tipo'] != 'Diretor' or dados_usuarios ['tipo'] == 'Professores' or (dados_usuarios ['tipo'] == 'Alunos' and dados_usuarios['id'] != int (dados_recebido_url['id'])):
        return 'Usuário não autorizado!', 403

    msg, status = validate_user_id(dados_recebido_url)
    if not status:
        return msg, 400
    
    dados_recebidos_corpo = request.json 
    msg, status  = aluno_up (dados_recebido_url['id'], dados_recebidos_corpo)

    return msg, status

@auth_rotas.route('/professor', methods=["POST"])
@validate_token
def criar_professor():
    dados_recebidos_url = request.args
    dados_usuarios = request.user
    if dados_usuarios ['tipo'] != 'Diretor':
        return 'Usuário não autorizado!', 403

    msg, status = validate_user_id(dados_recebidos_url)
    if not status:
        return msg, 400

    dados_recebidos_corpo = request.json 
    new_users = professor_cre (dados_recebidos_url['id'], dados_recebidos_corpo)
    
    return{
        'new_users_list': new_users
    }

@auth_rotas.route('/aluno', methods=["POST"])
@validate_token
def criar_aluno():
    dados_recebidos_url = request.args
    dados_usuarios = request.user
    if dados_usuarios ['tipo'] != ['Diretor'] and dados_usuarios ['tipo'] != 'Professores':
        return 'Usuário não autorizado!', 403
        
    msg, status = validate_user_id(dados_recebidos_url)
    if not status:
        return msg, 400

    dados_recebidos_corpo = request.json 
    new_users = aluno_cre (dados_recebidos_url['id'], dados_recebidos_corpo)
    
    return{
        'new_users_list': new_users
    }