def validate_create_conteudo(dados_recebidos):
    if 'nome' not in dados_recebidos:
        return 'Nome do conteudo é obrigatório', False
    
    if len(dados_recebidos['nome']) == 0:
        return 'Nome do conteudo não pode ser vazio', False
    
    return '', True