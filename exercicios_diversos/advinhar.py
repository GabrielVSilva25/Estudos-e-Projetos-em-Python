from random import randint
jogador = int(input('Informe um número de 0 a 5: '))

maquina = randint(0, 5)

if jogador == maquina:
    print(f'Você venceu, parabéns')

else:
    print('Tente novamente, você errou! :[')