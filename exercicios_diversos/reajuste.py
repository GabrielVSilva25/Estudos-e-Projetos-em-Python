salario = float(input('Informe o salário atual: '))

if salario < 0:
    print('Valor Inválido')

elif salario <= 280:
    ajuste = salario * 0.20

elif salario > 280 and salario <= 700:
    ajuste = salario * 0.15

elif salario > 700 and salario <= 1500:
    ajuste = salario * 0.10

else:
    ajuste = salario * 0.05

print(f'O salário foi ajustado para R${salario + ajuste}')   