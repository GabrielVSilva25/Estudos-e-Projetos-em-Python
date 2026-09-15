lista = ['Iphone X', 'Iphone 13', 'Iphone 14', 'Iphone 15','Iphone 16', 'Iphone 17']
vendas = [1000, 1890, 3200, 4900, 4600, 12000]

tamanho = len(lista)

print(f'Temos {tamanho} itens na lista')

mais_Vendido = max(vendas)
menos_Vendido = min(vendas)


print(f'O item mais vendido teve {mais_Vendido} unidades vendidas e o item menos vendido teve {menos_Vendido} unidades vendidas')

Produto_mais_Vendido = vendas.index(mais_Vendido)
Produto_menos_Vendido = vendas.index(menos_Vendido)

print(f'O produto mais vendido foi o {lista[Produto_mais_Vendido]} e o menos vendido foi o lista {lista[Produto_menos_Vendido]}')

