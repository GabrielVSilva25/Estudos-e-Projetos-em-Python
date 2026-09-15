# Crie um programa que solicite dois  valores numéricos, um numerador e um denominador, e retorne o resto da divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.
num1 = float(input('Informe um numerador maior que 0: '))
num2 = float(input('Informe o denominador: '))

divisao = num1 % num2 

print(f'O resto da divisao entre {num1} e {num2} é : {divisao}')
