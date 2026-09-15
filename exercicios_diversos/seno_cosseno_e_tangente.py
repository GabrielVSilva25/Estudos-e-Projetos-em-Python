from math import sin, cos, tan, radians
ang = int(input('Informe o ângulo que deseja: '))

seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))

print(f'O ângulo de {ang} tem o seno de {seno:.2f}')
print(f'O ângulo de {ang} tem o cosseno de {cosseno:.2f}')
print(f'O ângulo de {ang} tem a tangente de {tangente:.2f}')