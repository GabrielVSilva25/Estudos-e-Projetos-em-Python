
senha_cadastrada = input('Cadastre uma senha: ')
senha = ''

while senha != senha_cadastrada:
    senha = input('Digite a senha cadastrada para fazer login: ')

    if senha == senha_cadastrada:
        print('Bem-vindo!')

    else:
        print('Senha incorreta.')