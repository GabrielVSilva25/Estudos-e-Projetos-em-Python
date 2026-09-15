alimentos = 50
bebidas = 75
limpeza = 30

nome_produto = (input('Informe o nome do produto: '))
categoria = (input('Qual a categoria do produto? [alimentos / bebidas / limpeza]'))
qtd = int(input('Qual a quantidade: '))

if nome_produto and categoria and qtd:
    if categoria == alimentos:
        if qtd < alimentos:
            print(f'Solicitar {nome_produto} à equipe de compras, temos apenas {qtd} em estoque.')
        
    elif categoria == bebidas:
        if qtd < bebidas:
            print(f'Solicitar {nome_produto} à equipe de compras, temos apenas {qtd} em estoque.')

    else:
        if qtd < limpeza:
            print(f'Solicitar {nome_produto} à equipe de compras, temos apenas {qtd} em estoque.')
        
else: print('Por gentileza, preencha todos os campoos.')