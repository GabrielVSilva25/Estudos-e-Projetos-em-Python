# Escreva um programa que peça à pessoa usuária três números que representam os lados de um triângulo. O programa deve informar se os valores podem ser utilizados para formar um triângulo e, caso afirmativo, se ele é equilátero, isósceles ou escaleno. Tenha em mente algumas dicas:

# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes.


a = float(input("Digite o comprimento do primeiro lado: "))
b = float(input("Digite o comprimento do segundo lado: "))
c = float(input("Digite o comprimento do terceiro lado: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Os lados informados podem formar um triângulo.")

    if (a == b) and (b == c):
        print("O triângulo é Equilátero (todos os lados iguais).")
    elif (a == b) or (a == c) or (b == c):
        print("O triângulo é Isósceles (dois lados iguais).")
    else:
        print("O triângulo é Escaleno (todos os lados diferentes).")

else:
    print("Os lados informados NÃO podem formar um triângulo.")
