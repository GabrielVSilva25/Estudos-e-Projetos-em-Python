# Descobrir o maior entre três números.

numero1 = int(input('Informe um número: '))
numero2 = int(input('Informe outro número: '))
numero3 = int(input('Informe mais um número: '))

if numero1 > numero2 and numero1 > numero3:
    print(f'O número {numero1} é maior que o {numero2} e {numero3}')

elif numero2 > numero1 and numero2 > numero3:
    print(f'O número {numero2} é maior que o {numero1} e {numero3}')

else:
    print(f'O número {numero3} é maior que o {numero1} e {numero2}')
    