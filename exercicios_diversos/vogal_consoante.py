letra = input('Digite uma letra: ').upper().strip()

vogais = ['A, E, I, O, U']
consoantes = ['B', 'C', 'D', 'F',  'G',  'J',  'K',  'L',  'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']

if letra in vogais:
    print(f'Vogal')

elif letra in consoantes:
    print('Consoante')

else:
    print('Isso não se parece com uma vogal ou consoante.')