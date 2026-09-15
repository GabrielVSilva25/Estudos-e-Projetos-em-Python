# Crie um programa que sorteia, aleatoriamente, um número inteiro positivo menor que 100.
from random import randrange, sample

lista = []

for i in range(0, 100):
  lista.append(randrange(100))

print(lista)
