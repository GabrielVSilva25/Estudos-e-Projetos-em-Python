lista_produtos = []
lista_quantidades = []

# Solicitar produtos e qtdee em estoque
nome_produto = input('Informe o nome do produto: ')
lista_produtos.append(nome_produto)

qtd_estoque = int(input('Informe o valor em estoque: '))
lista_quantidades.append(qtd_estoque)

#Lista os produtos e as quantidades em estoque
print('===== Produtos =====')
for prod in range(len(lista_produtos)):
    print(f'{lista_produtos[prod]} - {lista_quantidades[prod]}')

#Buscar produtos em estoque
buscar = input('Informe o produto que deseja buscar no estoque: ')
for produto in lista_produtos:
    if buscar == produto:
        indice_produto = lista_produtos.index(produto)
        print(f'Produto encontrado - {lista_produtos[indice_produto]} - {lista_quantidades[indice_produto]}')
        break
else:
    print(f'O produto {buscar} não foi encontrado.')

    