# Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.

n1 = int(input('Informe 1 número inteiro: '))
n2 = int(input('Informe mais 1 número inteiro: '))

if n1 < n2:
    for i in range(n1+1, n2):
        print(i)
        
elif n2 < n1:
   for i in range(n2+1, n1):
        print(i)

else:
    print('Os números são iguais.')
