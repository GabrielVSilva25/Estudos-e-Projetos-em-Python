# Faça um programa que, ao inserir um número qualquer, cria uma lista contendo todos os números primos entre 1 e o número digitado.

num = int(input('Informe um número inteiro: '))


primos = []

# começando do 2, todo primo terá apenas 1 divisor (ele mesmo)
for i in range(2, num + 1):
    cont = 0

    for j in range(2, i + 1):
        if i % j == 0:
            cont+=1

    if cont == 1:
        primos.append(i)

print(f'Os números primos até {num} são: {primos}')
