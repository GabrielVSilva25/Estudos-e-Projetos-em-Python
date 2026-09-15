import random

contador = 0
computador = random.randint(1, 20)

jogador = int(input('Digite um número: '))
contador +=1

while computador != jogador:

    if jogador > 20 or jogador < 1:
        print('Por gentileza, tente novamente com números de 1 a 20.')  

    elif jogador > computador:
        print('Tente novamente! O número é menor.')

    else:
        print('Tente novamente! O número é maior')

    jogador = int(input('Digite um número: '))
    contador +=1

print(f'Foram realizadas {contador} tentativas.')
print('Parabéns, você acertou o número.')