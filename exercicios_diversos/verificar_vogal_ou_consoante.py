# Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.

vogal = 'a, e, i, o, u'

consoantes ='b, c, d, f, g, h, i, j, k, l, m, n, p, q, r, s, t, v, w, x, y, z'

letra = input('Digite uma letra: ')

if letra in vogal:
    print(f'A letra {letra} é uma vogal')

elif letra in consoantes:
    print(f'A letra {letra} é uma consoante')

else:
    print(f'Isso não é uma letra.')
