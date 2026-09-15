contador_notas = 0
soma_notas = 0

print('Digite -1 para encerrar o programa.')

nota = float(input('Digite uma nota: '))

while nota != -1:
    contador_notas +=1
    soma_notas += nota

    nota = float(input('Digite uma nota: '))

if nota == -1 and contador_notas == 0:
    print('Programa encerrado.')

else:
    print(f'\nQuantidade de Notas: {contador_notas}')
    print(f'Soma das notas: {soma_notas}')
    print(f'Média das notas: {soma_notas/(contador_notas)}')
