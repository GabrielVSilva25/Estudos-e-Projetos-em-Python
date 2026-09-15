opcao = int(input('''========= MENU =========

1 - Consultar saldo
2 - Depositar
3 - Sacar
4 - Extrato
5 - Sair

Escolha uma das opções: '''))

saldo = 1000
ultimo_deposito = 0
ultimo_saque = 0

while opcao != 5:
    if opcao == 1:
        print(f'O saldo atual é: R${saldo:.2f}')
        
    elif opcao == 2:
        ultimo_deposito = float(input('Digite o valor a ser depositado: R$'))

        if ultimo_deposito > 0:
            saldo += ultimo_deposito
            print(f'Saldo atualizado: {saldo}')

            opcao = int(input('''========= MENU =========
            
                        1 - Consultar saldo
                        2 - Depositar
                        3 - Sacar
                        4 - Extrato
                        5 - Sair
            
                        Escolha uma das opções: '''))

        else:
            print('Valor inválido, tente novamente.')
            opcao = int(input('''========= MENU =========

            1 - Consultar saldo
            2 - Depositar
            3 - Sacar
            4 - Extrato
            5 - Sair

            Escolha uma das opções: '''))

    elif opcao == 3:
        print(f'Saldo atual: {saldo}')
        ultimo_saque = float(input('Qual o valor que deseja sacar: R$ '))
        if ultimo_saque > saldo:
            print('Saldo insuficiente.')

            opcao = int(input('''========= MENU =========
            
            1 - Consultar saldo
            2 - Depositar
            3 - Sacar
            4 - Extrato
            5 - Sair

            Escolha uma das opções: '''))

        elif ultimo_saque <= 0:
            print('Valor inválido.')
            
            opcao = int(input('''========= MENU =========
            
            1 - Consultar saldo
            2 - Depositar
            3 - Sacar
            4 - Extrato
            5 - Sair

            Escolha uma das opções: '''))
            
        else:
            print('O valor de saque foi realizado. Aguarde..')
            saldo -= ultimo_saque
            print(f'O valor de saque foi R${ultimo_saque}, novo valor em conta atualizado R${saldo} ')

            opcao = int(input('''========= MENU =========
            
                        1 - Consultar saldo
                        2 - Depositar
                        3 - Sacar
                        4 - Extrato
                        5 - Sair
            
                        Escolha uma das opções: '''))

    elif opcao == 4:
        print(f'Ultimo saque realizado: R${ultimo_saque}')
        print(f'Ultimo depósito realizado: R${ultimo_deposito}')
        print(f'Saldo atual em conta: R${saldo}')

        opcao = int(input('''========= MENU =========
        
                    1 - Consultar saldo
                    2 - Depositar
                    3 - Sacar
                    4 - Extrato
                    5 - Sair
        
                    Escolha uma das opções: '''))

    else:
        print('A opção escolhida é invalida')

        opcao = int(input('''========= MENU =========

        1 - Consultar saldo
        2 - Depositar
        3 - Sacar
        4 - Extrato
        5 - Sair

        Escolha uma das opções: '''))

print('Programa encerrado.')