def mostrar_menu():

    menu = int(input(
'''========= MENU =========

1 - Consultar saldo
2 - Depositar
3 - Sacar
4 - Extrato
5 - Sair

Escolha uma das opções: '''))
    print('======================== \n')

    return menu

saldo = 1000
ultimo_deposito = 0
ultimo_saque = 0
opcao = mostrar_menu()

def mostrar_saldo(saldo):
    print(f'O saldo atual é R${saldo:.2f}\n')

def deposito():
    ultimo_deposito = float(input('Digite o valor a ser depositado: R$'))
    return ultimo_deposito

def saque():
    ultimo_saque = float(input('Qual o valor que deseja sacar: R$ '))
    return ultimo_saque

while opcao != 5:
    if opcao == 1:
        mostrar_saldo(saldo)
                
    elif opcao == 2:
        ultimo_deposito = deposito()

        if ultimo_deposito > 0:
            saldo += ultimo_deposito
            mostrar_saldo(saldo)

        else:
            print('Valor inválido, tente novamente.\n')

    elif opcao == 3:
        mostrar_saldo(saldo)
        ultimo_saque = saque()

        if ultimo_saque > saldo:
            print('Saldo insuficiente.\n')

        elif ultimo_saque <= 0:
            print('Valor inválido.\n')
            
        else:
            print('O valor de saque foi realizado. Aguarde...')

            saldo -= ultimo_saque
            print(f'O valor de saque foi R${ultimo_saque:.2f}')
            mostrar_saldo(saldo)

    elif opcao == 4:
        print(f'Ultimo saque realizado: R${ultimo_saque:.2f}')
        print(f'Ultimo depósito realizado: R${ultimo_deposito:.2f}')
        print(f'Saldo atual em conta: R${saldo:.2f}')

    else:
        print('A opção escolhida é invalida')

    opcao = mostrar_menu()

print('Programa encerrado.')