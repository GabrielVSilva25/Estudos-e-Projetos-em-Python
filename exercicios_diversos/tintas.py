metros_Quadrados = float(input('Informe o tamanho em m2 da área a ser pintada: '))

qtLitros = metros_Quadrados / 3

qtLatas = qtLitros / 18

if qtLitros % 18 == 0:
    qtLatas +=1

print(f'Será necessário {qtLatas} lata(s) para realizar a pintura da área informada.')
print(f'O valor total da compra é R${qtLatas * 80}')
