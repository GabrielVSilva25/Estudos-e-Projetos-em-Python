# Restaurante Python

# Crie um pequeno programa que mostre este menu:

# ========= MENU =========

# 1 - Hambúrguer - R$25

# 2 - Pizza - R$40

# 3 - Refrigerante - R$8

# 4 - Sair

# O usuário escolhe uma opção.

# O programa deve:

# mostrar qual produto foi escolhido;
# mostrar o preço;
# informar se a opção é inválida;
# encerrar quando escolher "Sair".

# Importante: ainda não use while. É apenas uma escolha por execução.

print('''
      ========= MENU =========

 1 - Hambúrguer - R$25
 2 - Pizza - R$40
 3 - Refrigerante - R$8
 4 - Sair
      ''')

opcao = int(input('Escolha uma opção do cardápio: '))

if opcao == 1:
    print('Você escolheu o Hambúrguer no valor de R$25')

elif opcao == 2:
    print('Você escolheu a Pizza no valor de R$40')

elif opcao == 3:
    print('Você escolheu o Refrigerante no valor de R$8')

elif opcao == 4:
    print('Sair')

else:
    print('Opcão inválida')
