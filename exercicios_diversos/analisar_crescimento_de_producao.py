# Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e informe se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).

producao = int(input('Digite o percentual de produção da empresa: '))

if producao > 0:
    print('a Produção da empresa teve crescimento.')

elif producao < 0:
    print('a Produção da empresa está em decrescimento.')

else:
    print('a Produção da empresa não está em descrecimento.')
