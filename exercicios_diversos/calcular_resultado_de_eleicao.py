# Em uma eleição para gerência em uma empresa com 20 pessoas colaboradoras, existem quatro candidatos(as). 
# Escreva um programa que calcule o(a) vencedor(a) da eleição. A votação ocorreu da seguinte maneira:

# Cada colaborador(a) votou em uma das quatro pessoas candidatas (que representamos pelos números 1, 2, 3 e 4).
# Também foram contabilizados os votos nulos (representados pelo número 5) e os votos em branco (representados pelo número 6).
# Ao final da votação, o programa deve exibir o número total de votos para cada candidato(a), os nulos e os votos em branco. Além disso, deve calcular e exibir a porcentagem de votos nulos em relação ao total de votos e a porcentagem de votos em branco em relação ao total de votos.

candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
nulo = 0
branco = 0


print('Para votar escolha o número referente ao candidato: ')
print('1 - Candidato')
print('2 - Candidato')
print('3 - Candidato')
print('4 - Candidato')
print('5 - Nulo')
print('6 - Branco')

for i in range(1, 21):
    voto = int(input('Informe o número do candidato : '))
   
    if voto == 1:
        candidato1 +=1

    elif voto == 2:
        candidato2 +=1

    elif voto == 3:
        candidato3+=1

    elif voto == 4:
        candidato4 +=1
    
    elif voto == 5:
        nulo +=1

    elif voto == 6:
        branco +=1
    

print(f'1 - Candidato : {candidato1} votos')
print(f'2 - Candidato : {candidato2} votos')
print(f'3 - Candidato : {candidato3} votos')
print(f'4 - Candidato : {candidato4} votos')
print(f'5 - Nulo : {nulo} votos')
print(f'6 - Branco : {branco} votos')

print(f'Tivemos uma porcentagem de {(nulo / 20):.2%} votos em nulo.')
print(f'Tivemos uma porcentagem de {(branco / 20):.2%} votos em branco.')

