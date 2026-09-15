#  Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual operação ele deseja realizar. O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, positivo ou negativo
#  e inteiro ou decimal.

numero1 = float(input('Informe um número: '))
numero2 = float(input('Informe mais um número: '))

print('1 - Verificar se os números são par ou ímpar / 2 - positivo ou negativo / 3 - para inteiro e decimal')

opcao = int(input('Informe a opcao desejada:'))

if opcao == 1:
    if numero1 % 2 == 0:
        print(f'O número {numero1} é par')
    else:
        print(f'O número {numero1} é ímpar')


    if numero2 % 2 == 0:
        print(f'O número {numero2} é par')
    else:
        print(f'O número {numero2} é ímpar')

elif opcao == 2:
    if numero1 > 0:
        print(f'O número {numero1} é positivo')
    else:
        print(f'O número {numero1} é negativo')

    if numero2 > 0:
        print(f'O número {numero2} é positivo')
    else:
        print(f'O número {numero2} é negativo')

    
elif opcao == 3:
    if numero1 % 1 == 0:
        print(f'O valor {numero1} é inteiro')
    else:
        print(f'O valor  {numero1} é real')

    if numero2 % 1 == 0:
        print(f'O valor {numero1} é inteiro')
    else:
        print(f'O valor {numero1} é real')


else:

    print('O valor informado não corresponde a uma das opções.')
