# Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada.

lista = []

for i in range(0,5):
    numero = int(input('Por gentileza, informe um número inteiro: '))

    lista.append(numero)


print(f'{lista[::-1]} números informados na lista.')
