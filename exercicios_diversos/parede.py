altura = float(input('Qual a altura da parede: '))
largura = float(input('Qual a largura da parede: '))

area = altura * largura

tinta = 2

litros = area / 2

print(f'A dimensão da parede é de {altura} x {largura}, a área é de {area}m², sendo necessário {litros}L de tinta para realizar a pintura da parede.')