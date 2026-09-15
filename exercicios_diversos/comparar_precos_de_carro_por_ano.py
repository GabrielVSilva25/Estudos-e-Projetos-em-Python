# Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos e exiba o valor mais alto e mais baixo entre esses três anos.

ano1 = 15.000
ano2 = 19.999
ano3 = 18.799

if ano1 > ano2 and ano1 > ano3:
    print('O Primeiro ano teve o valor mais alto')

elif ano2 > ano1 and ano2 > ano3:
    print('O Segundo ano teve o valor mais alto')

else:
    print('O Segundo ano teve o valor mais alto')
    

if ano1 < ano2 and ano1 < ano3:
    print('O Primeiro ano teve o valor mais baixo')

elif ano2 < ano1 and ano2 < ano3:
    print('O Segundo ano teve o valor mais baixo')

else:
    print('O Segundo ano teve o valor mais baixo')
    
