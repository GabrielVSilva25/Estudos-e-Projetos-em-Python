def pedir_idade():
    idade = int(input('Qual a sua idade? '))

    return idade


idade_atual = pedir_idade()
print(f'Daqui a 10 anos você terá {idade_atual + 10} anos.')