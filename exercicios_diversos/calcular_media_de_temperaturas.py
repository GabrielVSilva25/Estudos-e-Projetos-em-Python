# Desenvolva um programa que leia um conjunto indeterminado de temperaturas em Celsius e informe a média delas. A leitura deve ser encerrada ao ser enviado o valor -273°C.

temperatura = float(input('Informe a temperatura em Celsius: '))
print('Para finalizar o programa digite -273')

cont = 0
soma = 0

while temperatura != -273:
    soma += temperatura
    cont+=1

    temperatura = float(input('Informe a temperatura em Celsius: '))

media = soma / cont

print(f'A média das temperaturas foi de {media}')
