# Peça uma nota entre 0 e 10.

# Mostre:

# Reprovado (abaixo de 5)
# Recuperação (entre 5 e 6.9)
# Aprovado (7 ou mais)
# Desafio extra

# Caso o usuário digite:

# número negativo
# número maior que 10

nota = float(input('Informe a nota do aluno: '))

if nota < 0: 
    print('Número negativo')

elif nota > 10:
    print('Número maior que 10')

elif nota < 5:
    print('Reprovado')

elif nota >= 5 and nota < 7:
    print('Recuperação')

else:
    print('Aprovado')