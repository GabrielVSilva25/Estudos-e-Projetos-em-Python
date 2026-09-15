# Desenvolva um programa que informa a nota de um(a) aluno(a) de acordo com suas respostas. 
# Ele deve pedir a resposta desse(a) aluno(a) para cada questão e é preciso verificar se a resposta foi igual ao gabarito. 
# Cada questão vale um ponto e existem as alternativas A, B, C ou D.

gabarito = ['D','A','C','B','A','D','C','C','A','B']
respostas_Aluno = []

nota = 0
for i in range(1, len(gabarito)):
    respostas_Aluno.append(input(f'Informe a reposta da questão {i}: ').upper())

for i in range(1, len(gabarito)):
    if respostas_Aluno[i] == gabarito[i]:
        nota +=1

print(f'A nota final do aluno: [{nota}]')
 
