meta = 0.05
taxa = 0
rendimento = 0.01

if rendimento > meta:
    if rendimento > 0.20:
        taxa = 0.04
        print(f'A taxa foi de {taxa}')

    else:
        taxa = 0.02
        print(f'A taxa foi de {taxa}')

else:
    taxa = 0

    print(f'A taxa foi de {taxa}')
