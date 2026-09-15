idade = int(input('Informe a idade: '))

if idade < 12:
    print('Categoria: Infantil ')
    print('Ingresso: R$ 15')

elif idade < 17:
    print('Categoria: Adolescente ')
    print('Ingresso: R$ 20')

else: 
    print('Categoria: Adulto - ')
    print('Ingresso: R$ 30')