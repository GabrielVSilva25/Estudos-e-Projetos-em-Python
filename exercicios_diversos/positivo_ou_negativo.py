num = int(input('Digite um número positivo ou negativo: '))

if num > 0:
    print(f'O número {num} informado é positivo.')
elif num < 0:
    print(f'O número {num} informado é negativo.')
else:
    print(f'O número informado é igual a 0.')
