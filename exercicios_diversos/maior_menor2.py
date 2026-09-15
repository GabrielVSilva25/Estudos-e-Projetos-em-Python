a1 = int(input('Informe um número: '))
b1 = int(input('Informe mais um número: '))
c1 = int(input('Informe outro número: '))

if a1 > b1 and a1 > c1:
    print(f'O número{a1} é o maior valor ')

elif b1 > a1 and b1 > c1:
    print(f'O número{b1} é o maior valor ')

else:
    print(f'O número{c1} é o maior valor ')

if a1 < b1 and a1 < c1:
    print(f'O número{a1} é o menor valor ')

elif b1 < a1 and b1 < c1:
    print(f'O número{b1} é o menor valor ')

else:
    print(f'O número{c1} é o menor valor ')