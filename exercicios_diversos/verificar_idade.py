# 1. Verificador de idade

# O usuário informa a idade e o programa diz a classificação

# Regras:

# Menor que 12 → Criança
# Entre 12 e 17 → Adolescente
# Entre 18 e 59 → Adulto
# 60 ou mais → Idoso

idade = int(input('Informe a idade: '))

if idade < 12:
    print('Criança')

elif idade < 17:
    print('Adolescente')

elif idade < 59:
    print('Adulto')

else:
    print('Idoso')