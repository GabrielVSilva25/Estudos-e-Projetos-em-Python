# Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima de 3000 reais e calcule a porcentagem quanto ao 
# total de compras.

lista = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

tamanho_lista = len(lista)
cont3000 = 0

for gastos in lista:
    if gastos > 3000:
        cont3000 += 1

print(f'{cont3000 / tamanho_lista:.2%}% dos gastos foi acima de R$3000')
