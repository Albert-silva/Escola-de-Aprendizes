def login_validado(dados_recebidos):
    if not dados_recebidos.get('email'):
        return 'E-mail obrigatorio!', False

    if not dados_recebidos.get('senha'):
        return 'Senha obrigatorio!', False

    return '', True

def validate_user_id (dados_recebidos):
    if not dados_recebidos.get('id'):
        return 'O id é obrigatório', False
    return '', False 