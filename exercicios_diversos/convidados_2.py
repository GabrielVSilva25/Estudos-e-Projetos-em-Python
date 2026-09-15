lista_Convidados = ['José','Zilda','Gabriel']

mensagem = 'você foi convidado(a) para um jantar em um restaurante, hoje a noite.'

print(lista_Convidados[0] + ' ' + mensagem)
print(lista_Convidados[1] + ' ' + mensagem)
print(lista_Convidados[2] + ' ' + mensagem)

print(lista_Convidados[2] + ' não poderá comparecer.')

lista_Convidados.remove('Gabriel')
lista_Convidados.append('Paloma')

print(lista_Convidados[0] + ' ' + mensagem)
print(lista_Convidados[1] + ' ' + mensagem)
print(lista_Convidados[2] + ' ' + mensagem)