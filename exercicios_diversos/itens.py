itens = ['geladeira', 'fogão', 'celular', 'tablet']

consulta = input('Informe um itens para pesquisa: ')
if consulta in itens:
    i = consulta.index(itens)
    print(i)

else:
    print('Este produto não foi encontrado')

