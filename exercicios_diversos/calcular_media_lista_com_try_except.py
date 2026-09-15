# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

lista_Valores = [1, 5, 7, 9, 13, 14]
valores = 0

try:

    for valor in lista_Valores:

        valores += valor
        
        qtd_valores = len(lista_Valores)
        

    media = valores / qtd_valores

    print(f' A média dos valores é {media:.2f}')

except:
    print('Ocorreu um erro.')