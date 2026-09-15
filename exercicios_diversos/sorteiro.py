from random import choice 

nome_1 = input('Primeiro aluno: ')
nome_2 = input('Segundo aluno: ')
nome_3 = input('Terceiro aluno: ')
nome_4 = input('Quarto aluno: ')

lista = [nome_1, nome_2, nome_3, nome_4]

rand = choice(lista)

print(f'O aluno escolhido foi o {rand}.')

