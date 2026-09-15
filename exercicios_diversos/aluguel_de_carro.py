km = int(input('Quantos KM foram percorridos? '))
dias = float(input('Qual a quantidade de dias alugados? '))

valor = (km*0.15) + (dias*60)

print(f'O total a ser pago é R${valor:.2f}')