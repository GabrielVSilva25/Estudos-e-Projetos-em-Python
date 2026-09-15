# Faça um código que colete em uma lista 5 números inteiros quaisquer e imprima a lista. Exemplo: [1,4,7,2,4]

lista = []

for i in range(0,5):
    numero = int(input('Por gentileza, informe um número inteiro: '))

    lista.append(numero)


print(f'{lista} números informados na lista.')
