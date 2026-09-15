# Vamos entender a distribuição de idades de pensionistas de uma empresa de previdência. 
# Escreva um programa que leia as idades de uma quantidade não informada de clientes e mostre a distribuição em intervalos de [0-25], 
# [26-50], [51-75] e [76-100]. Encerre a entrada de dados com um número negativo.

idade = int(input('Informe a idade: '))

cont25 = 0
cont50 = 0
cont75 = 0
cont100 = 0

while idade > 0:

    if idade > 0 and idade <= 25:
        cont25 +=1
    elif idade > 25 and idade <= 50:
        cont50 +=1
    elif idade > 50 and idade <= 75:
        cont75 +=1
    elif idade > 75 and idade <= 100:
        cont100 +=1
    
    idade = int(input('Informe a idade: '))

print('Distribuição de idades: ')

print('De 0 - 25: ', cont25)
print('De 26 - 50: ', cont50)
print('De 51 - 75: ', cont75)
print('De 76 - 100: ', cont100)
