from datetime import datetime
from flask import Blueprint, request

from modules.auth.validacao import login_validado

auth_rotas = Blueprint ('auth', __name__)

Diretores = [
    {
        'Nome': 'Beto',
        'cpf': 12345678910,
        'id': 1,
        'E-mail': 'carlosnoronha@eaprendizes.com',
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
        'E-mail': 'marcoshefa@eaprendizes.com',
        'senha': 963852,
        'created_at': datetime(2022, 5, 1, 12, 0),
        'updated_at': datetime(2022, 5, 1, 12, 0),
     }
]
Alunos = [
    { 
        'Nome': 'Albert',
        'E-mail': 'albert@eaprendizes.com',
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
        if user['E-mail'] == dados_recebido['email']:
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
        if user['E-mail'] == dados_recebido['E-mail']:
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
        if user['E-mail'] == dados_recebido['E-mail']:
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