# Para uma seleção de produtos alimentícios, precisamos separar o conjunto de IDs dados por números inteiros sabendo que os produtos com 
# ID par são doces e os com ID ímpar são amargos. Monte um código que colete 10 IDs. Depois, calcule e mostre a quantidade de produtos 
# doces e amargos.

id_doces = []
id_amargos = []

for i in range(0, 10):
    produtos = int(input('Informe um ID :'))

    if produtos % 2 == 0:
        id_doces.append(produtos)
    
    else:
        id_amargos.append(produtos)



print(f'Dos produtos informados temos: {len(id_doces)} Doces e {len(id_amargos)} Amargos.')
