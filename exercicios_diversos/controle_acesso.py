nome = input('Informe seu nome: ')
idade = int(input('Qual a sua idade? '))

if idade < 18:
    print('Acesso negado.')

else:
    print(f'Bem vindo(a), {nome}!')