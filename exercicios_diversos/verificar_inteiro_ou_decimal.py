# Escreva um programa que peça um número à pessoa usuária e informe se ele é inteiro ou decimal.

numero = float(input('Informe um número: '))

if numero % 1 == 0:
    print(f'Este número {numero} é inteiro')

else:
    print(f'Este número {numero} é real')

