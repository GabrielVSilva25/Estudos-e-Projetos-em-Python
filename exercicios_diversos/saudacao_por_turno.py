# Escreva um programa que pergunte em qual turno a pessoa usuária estuda ("manhã", "tarde" ou "noite") e exiba a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!", ou "Valor Inválido!", conforme o caso.1
print('manhã, tarde ou noite')
turno = input('Qual turno você estuda? ').lower()

if turno == 'manhã':
    print('Bom dia')

elif turno == 'tarde':
    print('Boa tarde')

elif turno == 'noite':
    print('Boa noite')
