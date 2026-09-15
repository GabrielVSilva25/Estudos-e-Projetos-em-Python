# Descobrir o maior entre dois números.

numero1 = int(input('Informe um número: '))
numero2 = int(input('Informe outro número: '))

if numero1 > numero2:
    print(f'O número {numero1} é maior que o {numero2}')

elif numero2 > numero1:
    print(f'O número {numero2} é maior que o {numero1}')

else:
    print('Os números informados são iguais.')
