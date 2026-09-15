num1 = int(input('Informe um número: '))
num2 = int(input('Informe outro número: '))
num3 = int(input('Informe mais outro número: '))

if num1 > num2 and num1 > num3:
    print(f'O {num1} é maior que os valores {num2} e {num3}')

elif num2 > num1 and num2 > num3:
    print(f'O {num2} é maior que os valores {num1} e {num3}')

elif num3 > num1 and num3 > num2:
    print(f'O {num3} é maior que os valores {num1} e {num2}')


if num1 < num2 and num1 < num3:
    print(f'O {num1} é menor que os valores {num2} e {num3}')

elif num2 < num1 and num2 < num3:
    print(f'O {num2} é menor que os valores {num1} e {num3}')

elif num3 < num1 and num3 < num2:
    print(f'O {num3} é menor que os valores {num1} e {num2}')
