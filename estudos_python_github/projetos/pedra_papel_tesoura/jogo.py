# Exercício 5 — Pedra, Papel ou Tesoura ⭐⭐⭐⭐
# 
# Ainda sem laços.
# 
# Ainda sem funções.
# 
# Mas quero que você tente montar toda a lógica.


import random

escolha_jogador = int(input('''
1 - Tesoura
2 - Pedra
3 - Papel
Escolha uma opcao acima: '''))

escolha_computador = random.randint(1,3)

if escolha_computador == 1:
    print('\nO computador escolheu Tesoura')

elif escolha_computador == 2:
    print('\nO computador escolheu Pedra')

else:
    print('\nO computador escolheu Papel')


if escolha_jogador > 3 or escolha_jogador < 1:
    print('Escolha errada, por gentileza, tentar novamente com uma opção válida.')

elif escolha_jogador == escolha_computador:
    print('Empate')

elif escolha_jogador == 1 and escolha_computador == 2 or escolha_jogador == 2 and escolha_computador == 3 or escolha_jogador == 3 and escolha_computador == 1:
    print('A Computador venceu.')
    print('Resultado - Computador 1x0 Jogador ')

else:
    print('O Jogador venceu')
    print('Resultado - Jogador 1x0 Computador ')