from flask import Blueprint, request
from API.decorators import validate_token
from API.modules.conteudo.controllers import lista_conteudos, seleciona_conteudo, deleta_conteudo, cria_conteudo, atualiza_conteudo, aluno_conteudo, conteudo_aluno, cria_aluno_conteudo
from API.modules.conteudo.validacao import validate_create_conteudo

conteudo_rotas = Blueprint ('conteudo', __name__, url_prefix="/conteudo")

@conteudo_rotas.route('/', methods=["GET"])
@validate_token
def lista_conteudos_route():
    user_id = None
    if request.user['tipo'] == 'Alunos':
        user_id = request.user['id']

    conteudos = lista_conteudos(user_id)

    return {
        "conteudos": conteudos
    }

@conteudo_rotas.route('/<id>', methods=["GET"])
@validate_token
def seleciona_conteudo_route(id):
    msg, status_code = seleciona_conteudo(id)
    if status_code > 300:
        return {
            "error": msg
        }, status_code

    return msg, status_code

@conteudo_rotas.route('/<id>', methods=["DELETE"])
@validate_token
def deleta_conteudo_route(id):
    dados_usuario = request.user
    if dados_usuario['tipo'] == 'Aluno':
        return 'Sem permissão!', 403

    msg, status_code = deleta_conteudo(id)
    if status_code > 300:
        return {
            "error": msg
        }, status_code
    
    return {
        "message": msg
    }, status_code

@conteudo_rotas.route('/<id>', methods=["PUT"])
@validate_token
def atualiza_conteudo_route(id):
    dados_usuario = request.user
    if dados_usuario['tipo'] == 'Aluno':
        return 'Sem permissão!', 403

    dados_recebidos = request.json

    msg, status_code = atualiza_conteudo(id, dados_recebidos)
    if status_code > 300:
        return {
            "error": msg
        }, status_code
    
    return {
        "message": msg
    }, status_code


@conteudo_rotas.route('/', methods=["POST"])
@validate_token
def cria_conteudo_route():
    dados_usuario = request.user
    if dados_usuario['tipo'] == 'Aluno':
        return 'Sem permissão!', 403

    dados_recebidos = request.json

    msg, status = validate_create_conteudo(dados_recebidos)
    if not status:
        return {
            "error": msg
        }, 400

    msg, status_code = cria_conteudo(dados_recebidos)
    if status_code > 300:
        return {
            "error": msg
        }, status_code

    return {
        "message": msg
    }, status_code

@conteudo_rotas.route('/criaalunoconteudo/', methods=["POST"])
@validate_token
def cria_conteudoaluno_route():
    dados_usuario = request.user
    if dados_usuario['tipo'] == 'Aluno':
        return 'Sem permissão!', 403

    dados_recebidos = request.json

    msg, status_code = cria_aluno_conteudo(dados_recebidos)
    if status_code > 300:
        return {
            "error": msg
        }, status_code

    return {
        "message": msg
    }, status_code

@conteudo_rotas.route('/conteudoaluno/<id_conteudo>', methods=["GET"])
@validate_token
def aluno_conteudo_route(id_conteudo):
    dados_usuario = request.user
    if dados_usuario['tipo'] == 'Aluno':
        return 'Sem permissão!', 403

    resultado = aluno_conteudo(id_conteudo)

    return {
        "conteudo_aluno": resultado
    }

@conteudo_rotas.route('/alunoconteudo/<id_aluno>', methods=["GET"])
@validate_token
def conteudo_aluno_route(id_aluno):
    dados_usuario = request.user
    if dados_usuario['tipo'] == 'Aluno':
        return 'Sem permissão!', 403

    resultado = conteudo_aluno(id_aluno)

    return {
        "aluno_conteudo": resultado
    }