# Calcular o preço total de uma compra.

qtd = int(input('Digite a quantidade do produto: '))
preco_Item = float(input('Digite o preço do produto: '))

total = qtd * preco_Item

print(F'O preço total da compra é: R${total:.2f}')