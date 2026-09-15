# Os números primos possuem várias aplicações dentro da Ciência de Dados em criptografia e segurança, por exemplo. 
# Um número primo é aquele que é divisível apenas por um e por ele mesmo. Assim, faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

numero = int(input('Digite um número inteiro: '))

cont = 0
for i in range(1, numero + 1):

    if numero % 1 == 0:
        cont +=1
    

if cont == 2:
    print(f'O número {numero} é primo')

else:
    print(f'O número {numero} não é primo')
