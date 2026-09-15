# Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas de crescimento de 3% e 1,5% respectivamente. 
# Considere que a colônia A inicia com 4 elementos e a B com 10.

a = 4
b = 10

taxaA = 0.03
taxaB = 0.015
cont = 0

while a < b:

  a = 1 * taxaA
  b = 1 * taxaB
  
  cont+=1
  if a >= b:
    print(f'Levaram cerca de {cont} dias para a colônia A ficar maior ou igual a colônia B')
