# Uma professora precisa de um programa que ajude a calcular a média final dos alunos e informe se foram aprovados, ficaram de recuperação ou reprovados. As regras são:

# Média >= 7: Aprovado
# 5 <= Média < 7: Recuperação
# Média < 5: Reprovado
# Escreva um programa que receba três notas como entrada e calcule a média final. Com base na média, exiba a situação do aluno.

n1 = float(input('Informe a 1° nota do aluno: '))
n2 = float(input('Informe a 1° nota do aluno: '))
n3 = float(input('Informe a 1° nota do aluno: '))

media = (n1 + n2+ n3) / 3

if media < 5:
    print('Reprovado')

elif media <= 5 and media < 7:
    print('Recuperação')

else:
    print('Aprovado')
