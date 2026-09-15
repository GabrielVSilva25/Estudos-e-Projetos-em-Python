# Você está desenvolvendo um sistema de controle de estoque para o Buscante. Um dos requisitos é verificar a quantidade de exemplares de um livro em estoque e continuar vendendo até que o estoque se esgote.
# Sempre que uma venda é realizada, o sistema deve informar o usuário e atualizar a quantidade disponível.
# Crie um programa que simule as vendas de um livro com o estoque inicial de 5 exemplares. O programa deve exibir a mensagem "Venda realizada! Estoque restante: <quantidade>" a cada venda e, ao final, exibir a mensagem "Estoque esgotado".

qtd_Livro = 5

while qtd_Livro > 0:
    qtd_Venda = int(input('Informe a quantidade de livros para compra: '))
    qtd_Livro -= qtd_Venda
    print(f'Venda Realizada! Estoque restante {qtd_Livro}')

print('Estoque esgotado')