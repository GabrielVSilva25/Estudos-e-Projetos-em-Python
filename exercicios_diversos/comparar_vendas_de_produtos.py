# Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais. Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.

maças = int(input('Digite a quantidade de maças vendidas: '))
bananas = int(input('Digite a quantidade de bananas vendidas: '))

if maças > bananas:
    print('As maças tiveram mais vendas.')

elif bananas > maças:
    print('As bananas tiveram mais vendas.')

else:
    print('As maças e bananas tiveram a mesma quantidade vendida.')