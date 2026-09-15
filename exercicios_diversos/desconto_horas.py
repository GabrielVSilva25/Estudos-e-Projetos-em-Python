horas = int(input('Quantas horas foram trabalhadas este mês? '))
pHora = float(input('Quanto recebe por hora? '))

salario = horas * pHora

ir = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05

desconto = ir + inss + sindicato

print(f'Salário bruto - R$ {salario:.2f}')
print(f'INSS - R${inss:.2f}')
print(f'IR - R${ir:.2f}')
print(f'Sindicato - R${sindicato:.2f}')

print(f'Salário líquido - R${salario - desconto:.2f}')
