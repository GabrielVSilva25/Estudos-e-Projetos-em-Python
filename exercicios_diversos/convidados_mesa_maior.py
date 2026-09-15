lista_Convidados = ['José','Zilda','Gabriel']

mensagem = 'você foi convidado(a) para um jantar em um restaurante, hoje a noite.'

print(lista_Convidados[0] + ' ' + mensagem)
print(lista_Convidados[1] + ' ' + mensagem)
print(lista_Convidados[2] + ' ' + mensagem)

print(lista_Convidados[2] + ' não poderá comparecer.')

print(' ------------------------------- ')
lista_Convidados.remove('Gabriel')
lista_Convidados.append('Paloma')

print(lista_Convidados[0] + ' ' + mensagem)
print(lista_Convidados[1] + ' ' + mensagem)
print(lista_Convidados[2] + ' ' + mensagem)

print(' ------------------------------- ')

lista_Convidados.insert(0,'Bruna')
lista_Convidados.append('Karin')

print(lista_Convidados[0] + ' ' + mensagem)
print(lista_Convidados[1] + ' ' + mensagem)
print(lista_Convidados[2] + ' ' + mensagem)
print(lista_Convidados[3] + ' ' + mensagem)
print(lista_Convidados[4] + ' ' + mensagem)

print(' ------------------------------- ')

desconvidar = 'Houve um problema com a minha reserva, infelizmente vou precisar cancelar.'

print(lista_Convidados[0] + ' ' + desconvidar)
lista_Convidados.pop(0)

print(lista_Convidados[3] + ' ' + desconvidar)
lista_Convidados.pop(3)

print(lista_Convidados[2] + ' ' + desconvidar)
lista_Convidados.pop(2)


lista_Convidados.pop(1)
lista_Convidados.pop(0)
print(lista_Convidados)

