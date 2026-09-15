# Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.

p1 = float(input('Qual o valor do primeiro produto? '))
p2 = float(input('Qual o valor do segundo produto? '))
p3 = float(input('Qual o valor do terceiro produto? '))

if p1 < p2 and p1 < p3:
    print(f'O produto mais barato é o primeiro, custando R${p1}')

elif p2 < p1 and p2 < p3:
    print(f'O produto mais barato é o segundo, custando R${p2}')

else:
    print(f'O produto mais barato é o terceiro, custando R${p3}')
