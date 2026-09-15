nome = str(input('Digite seu nome completo: ')).strip()

print(f'Seu nome maiusculo {nome.upper()}')
print(f'Seu nome minusculo {nome.lower()}')
print(f'Seu nome contém {len(nome)-nome.count(' ')} letras')
print(f'Seu primeiro nome tem {nome.find(' ')}')