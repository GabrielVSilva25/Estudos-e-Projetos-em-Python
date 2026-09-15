turno = input('M-matutino ou V-Vespertino ou N- Noturno \nQual horário você estuda? ').upper().strip()

if turno == 'M':
    print('Bom diaa!')

elif turno == 'V':
    print('Boa tarde!') 

elif turno == 'N':
    print('Boa noite!')

else:
    print('Valor inválido.')
