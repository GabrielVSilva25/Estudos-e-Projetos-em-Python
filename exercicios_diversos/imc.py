
# peso
# altura

# Calcule o IMC.

# Informe a classificação.

# Não precisa decorar a tabela. Você pode pesquisar apenas os intervalos do IMC, já que o objetivo do exercício é praticar as condições, não memorizar valores.
imc = 0

peso = float(input('Informe o peso: '))
altura = float(input('Informe a altura: '))

imc = peso / (altura * altura)

print(f'{imc:.2f}')

if imc < 18.5:
    print('Baixo peso')

elif imc >= 18.5 and imc < 25:
    print('Peso normal')

elif imc >= 25 and imc < 30:
    print('Sobrepeso')

elif imc >= 30 and imc < 35:
    print('Obesidade grau I')

elif imc >= 35 and imc < 40:
    print('Obesidade grau II')

else:
    print('Obesidade grau III (Grave)')

