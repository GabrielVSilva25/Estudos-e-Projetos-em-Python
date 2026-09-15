from random import randint

tup = (randint(1, 15),randint(1, 15),randint(1, 15),randint(1, 15),randint(1, 15))

print(f'OS número sorteados foram: ')

for i in tup:
    print(f'{i}', end=' ')

print(f'\nO maior valor é {max(tup)}')
print(f'O menor valor é {min(tup)}')
