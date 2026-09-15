km = float(input('Qual a distancia (km) da viagem? '))

if km <= 200:
    valor = km * 0.50
else:
    valor = km * 0.45

print(f'Uma viagem de {km}km, fica no valor de R${valor}.')