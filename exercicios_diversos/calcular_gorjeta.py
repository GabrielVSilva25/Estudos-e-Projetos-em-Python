valor_conta = float(input('Informe o valor da conta: '))
gorjeta = int(input('Informe a porcentagem de gorjeta: '))

valor_gorjeta = valor_conta * (gorjeta / 100)
valor_total = valor_conta + valor_gorjeta

print(f'Valor da gorjeta: R$ {valor_gorjeta}')
print(f'Total a pagar: R$ {valor_total}')