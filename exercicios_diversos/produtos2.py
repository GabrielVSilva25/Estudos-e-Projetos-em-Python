lista = ['Iphone X', 'Iphone 13', 'Iphone 14', 'Iphone 15','Iphone 16', 'Iphone 17']

lista.append('Iphone XR')

print(lista)

remover = 'Iphone X'

if remover in lista:
    lista.remove(remover)
    print(lista)
else:
    print('Este item não está na lista')