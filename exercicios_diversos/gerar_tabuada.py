# Escreva um programa que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. Como exemplo, para o número 2, a tabuada deve ser mostrada no seguinte formato:

numero = int(input('Informe um número inteiro: '))

for i in range(1, 11):
    print(f'{numero} x {i} = {numero*i}')
