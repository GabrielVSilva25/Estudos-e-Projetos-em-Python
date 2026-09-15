salario = float(input('Qual o salário atual? R$ '))

if salario > 1250:

    salario = salario + (salario * 0.10)
else:
    salario = salario + (salario * 0.15)

print(f'O salário teve reajuste para R${salario}')
