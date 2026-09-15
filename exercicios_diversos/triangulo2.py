lado_1 = int(input('Informe o 1° lado do triângulo: '))
lado_2 = int(input('Informe o 2° lado do triângulo: '))
lado_3 = int(input('Informe o 3° lado do triângulo: '))

#Verificação da Desigualdade triangular
if lado_1 < lado_2 + lado_3 and lado_2 < lado_1 + lado_3 and lado_3 < lado_2 + lado_1 and lado_1 > lado_2 + lado_3 and lado_2 > lado_1 + lado_3 and lado_3 > lado_2 + lado_1:
    if lado_1 == lado_2 and lado_2 == lado_3:
        print('Os valores informados formam um Triângulo equilátero, todos os lados são iguais')

    elif lado_1 == lado_2 or lado_2 == lado_3 or lado_1 == lado_3:
        print('Os valores informados formam um Triângulo isósceles, dois dos lados são iguais')

    else:
        print('Os valores informados formam um Triângulo escaleno, todos os lados são diferentes')

else:
    print('Não é possível gerar um triângulo.')