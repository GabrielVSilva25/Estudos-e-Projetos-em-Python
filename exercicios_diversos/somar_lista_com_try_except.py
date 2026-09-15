# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

soma_Valores = 0
lista_Numeros = [1, 10, 50, 70 ,21, 33, 99,74, 1804]

try:
    for numero in lista_Numeros:
        soma_Valores += numero
    print(f'A soma dos valores foi de {soma_Valores}')

except:
    print('Ocorreu um erro')
