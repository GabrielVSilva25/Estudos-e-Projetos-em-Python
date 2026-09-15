from math import hypot

co = float(input('Informe o comprimento de cateto oposto: '))
ca = float(input('Informe o comprimento do cateto adjacente: '))

hi = hypot(co, ca)

print(f'O tamanho da hipotenusa é {hi:.2f}')