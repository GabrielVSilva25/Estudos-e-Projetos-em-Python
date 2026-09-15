import random
opcao = int(input('''========= MENU =========

1 - Dizer Olá
2 - Mostrar uma mensagem
3 - Gerar número aleatório
4 - Sair

Escolha uma opção: '''))

while opcao != 4:
    
    if opcao == 1:
        print("Olá! Como você está?")

    elif opcao == 2:
        mensagem = input("Digite a mensagem que deseja mostrar: ")
        print(f"A mensagem é: {mensagem}")

    elif opcao == 3:
        numero_aleatorio = random.randint(1, 100)
        print(f"Número aleatório gerado: {numero_aleatorio}")

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

    opcao = int(input('''========= MENU =========

            1 - Dizer Olá
            2 - Mostrar uma mensagem
            3 - Gerar número aleatório
            4 - Sair

            Escolha um opção: '''))

print("Saindo do programa. Até logo!")