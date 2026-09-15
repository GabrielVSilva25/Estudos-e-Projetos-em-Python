lado1 = float(input('Tamanho Lado 1: ')) 
lado2 = float(input('Tamanho Lado 2: ')) 
lado3 = float(input('Tamanho Lado 3: ')) 

if lado1 < lado2 + lado3 or lado2 < lado1 + lado3 or lado3 < lado2 + lado1:
    print(f'É possível formar um triângulo.')   

else:
    print(f'Não é possível formar um triângulo')

