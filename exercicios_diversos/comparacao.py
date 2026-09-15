faturamento_Loja1 = 2500
faturamento_Loja2 = 2200
email = 'email@gmail.com'

if faturamento_Loja1 == faturamento_Loja2:
    print('Os faturamentos são iguais.')

else:
    print('Os faturamentos são diferentes.')


if email == 'email2@gmail.com':
    print('Email correto!')

else: 
    print('Email errado!')


email_usuario = input('Insira seu e-mail: ')

if not '@' in email_usuario:
    print('Este e-mail é inválido.')

else:
    pass