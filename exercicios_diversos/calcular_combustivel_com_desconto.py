# Um estabelecimento está vendendo combustíveis com descontos variados. Para o etanol, se a quantidade comprada for até 15 litros, o desconto será de 2% por litro. Caso contrário, será de 4% por litro. Para o diesel, se a quantidade comprada for até 15 litros, o desconto será de 3% por litro. Caso contrário, será de 5% por litro. O preço do litro de diesel é R$ 2,00 e o preço do litro de etanol é R$ 1,70. Escreva um programa que leia a quantidade de litros vendidos e o tipo de combustível (E para etanol e D para diesel) e calcule o valor a ser pago pelo cliente. Tenha em mente algumas dicas:

# O do valor do desconto será a multiplicação entre preço do litro, quantidade de litros e o valor do desconto.
# O valor a ser pago por um cliente será o resultado da multiplicação do preço do litro pela quantidade de litros menos o valor de desconto resultante do cálculo.


preco_etanol = 1.70
preco_diesel = 2.00

tipo_combustivel = input("Digite o tipo de combustível (E para etanol e D para diesel): ").upper()
quantidade_litros = float(input("Digite a quantidade de litros vendidos: "))

valor_bruto = 0
percentual_desconto = 0

if tipo_combustivel == 'E':
    valor_bruto = preco_etanol * quantidade_litros
    if quantidade_litros <= 15:
        percentual_desconto = 0.02
    else:
        percentual_desconto = 0.04
elif tipo_combustivel == 'D':
    valor_bruto = preco_diesel * quantidade_litros
    if quantidade_litros <= 15:
        percentual_desconto = 0.03
    else:
        percentual_desconto = 0.05
else:
    print("Tipo de combustível inválido.")
    exit()

valor_desconto = valor_bruto * percentual_desconto
valor_total_a_pagar = valor_bruto - valor_desconto

print(f"Valor total a pagar: R$ {valor_total_a_pagar:.2f}")
