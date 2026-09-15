# Crie um programa que solicite à pessoa usuária digitar dois números inteiros e calcular a potência do 1º número elevado ao 2º.

from math import pow

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))

pow(n1, n2)

print(f'{n1} elevado a {n2} é igual a {pow(n1, n2)}')

