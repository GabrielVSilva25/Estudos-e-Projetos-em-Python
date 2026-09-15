peso_peixes = int(input('Qual o peso dos peixes? '))

if peso_peixes > 50:
    excedente = peso_peixes - 50

multa = excedente * 4

print(f'O valor da multa dessa vez foi de R${multa:.2f}')
