# Escreva um programa que leia três números e os exiba em ordem decrescente.

n1 = float(input('Informe um número? '))
n2 = float(input('Informe mais um número? '))
n3 = float(input('Informe outro número? '))

if n1 > n2 and n2 > n3 :
    print(f'Ordem descrescente: {n1}, {n2}, {n3}')

elif n2 > n1 and n1 > n3:
    print(f'Ordem descrescente: {n2}, {n1}, {n3}')

elif n3 > n1 and n1 > n2:
    print(f'Ordem descrescente: {n3}, {n1}, {n2}')

elif n2 > n3 and n3 > n1:
    print(f'Ordem descrescente: {n2}, {n3}, {n1}')

else:
    print(f'Ordem descrescente: {n3}, {n2}, {n1}')
