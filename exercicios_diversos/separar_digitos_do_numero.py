numero = int(input('Informe um número: '))

unid = numero // 1 % 10
cent = numero // 10 % 10
dezena = numero // 100 % 10
mil = numero // 1000 % 10

print(f'Unidade: {unid}')
print(f'Centena: {cent}')
print(f'Dezena: {dezena}')
print(f'Milhar: {mil}')

