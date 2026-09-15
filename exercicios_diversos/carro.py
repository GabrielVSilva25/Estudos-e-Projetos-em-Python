velocidade = int(input('Informe a velocidade do veículo: '))

permitido = 80

if velocidade >= permitido:
    maior = velocidade - permitido
    valor = maior * 7

    print(f'Você foi multado! \nO limite da via é 80km, você estava a {maior}km além do limite permitido, a multa será no valor de R${valor}')
print('Boa viagem!')