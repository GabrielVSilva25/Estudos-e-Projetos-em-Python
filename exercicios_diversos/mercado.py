nome_prod = input('Qual o nome do produto: ')
qtd_produto = int(input('Qual a quantidade: '))
preco_unitario = float(input('Qual o valor unitário do produto: '))

desc300 = 0.15
desc150 = 0.10
desconto = 0

subtotal = qtd_produto * preco_unitario

if subtotal > 300:
    desconto = subtotal * desc300
    print(f'O total foi de R${subtotal-desconto}')

elif subtotal > 150:
    desconto = subtotal * desc150
    print(f'O total foi de R${subtotal-desconto}')

else:
    print(f'O total foi de R${subtotal-desconto}')
