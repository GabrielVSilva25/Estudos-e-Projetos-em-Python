num = (int(input('Digite o primeiro valor: ')),
       int(input('Digite o segundo valor: ')),
       int(input('Digite o terceiro valor: ')),
       int(input('Digite o último valor: ')))

print(f'O número 9 apareceu {num.count(9)} vezes.')

if 3 in num:
    print(f'O primeiro número 3 aparece na {num.index(3)+1}ª posição.')

for n in num:
    if n % 2 ==0:
        print(f'Os números pares são {n}')
