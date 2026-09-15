nome = input('Qual o seu nome? ')
email = input('Informe seu e-mail: ')


if nome and email:
    pos_a = email.find('@')
    mail = email[pos_a:]

    if pos_a != -1 and '.' in mail:
        print('Seu cadastro foi concluído')
    else:
        print('Digite seu nome e email válidos.')
else:
    print('Digite seu nome e email válidos.') 