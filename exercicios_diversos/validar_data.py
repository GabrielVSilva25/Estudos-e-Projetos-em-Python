# Escreva um programa que peça uma data informando o dia, mês e ano e determine se ela é válida para uma análise.

dia = int(input('Informe o dia: '))
mes = int(input('Informe o mês: '))
ano = int(input('Informe o ano: '))

bissexto = False
dias_31 = [1, 3, 5, 7, 8, 10, 12]
dias_30 = [4, 6, 9, 11]

if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    bissexto = True

if mes < 1 or mes > 12:
    print(f'O mês {mes} é inválido.')

elif dia < 1:
    print(f'O dia {dia} é inválido.')

elif mes == 2:
    if (bissexto and dia <= 29) or (not bissexto and dia <= 28):
        print(f'A data {dia}/{mes}/{ano} é válida.')
    else:
        print(f'A data {dia}/{mes}/{ano} é inválida.')

elif mes in dias_30:
    if dia <= 30:
        print(f'A data {dia}/{mes}/{ano} é válida.')
    else:
        print(f'A data {dia}/{mes}/{ano} é inválida.')

elif mes in dias_31:
    if dia <= 31:
        print(f'A data {dia}/{mes}/{ano} é válida.')
    else:
        print(f'A data {dia}/{mes}/{ano} é inválida.')
