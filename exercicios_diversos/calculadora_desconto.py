# 2. Calculadora de desconto 

# O usuário informa o valor da compra.

# Regras:

# Até R$100 → Sem desconto
# Até R$500 → 10% de desconto
# Acima de R$500 → 20% de desconto

valorDesconto = 0

valor_Compra = float(input('Informe o valor total da compra: '))

if valor_Compra < 100:
    print('Sem desconto')
    print(f'O valor total da compra foi de R${valor_Compra:.2f}')

elif valor_Compra < 500:
    print('Desconto de 10% na compra')
    valorDesconto = valor_Compra * 0.1
    
    print(f'O valor do desconto foi de R${valorDesconto:.2f}')
    print(f'O valor total da compra foi de R${valor_Compra - valorDesconto:.2f}')

else:
    print('Desconto de 20% na compra')

    valorDesconto = valor_Compra * 0.2
    print(f'O valor do desconto foi de R${valorDesconto:.2f}')
    print(f'O valor total da compra foi de R${valor_Compra - valorDesconto:.2f}')
