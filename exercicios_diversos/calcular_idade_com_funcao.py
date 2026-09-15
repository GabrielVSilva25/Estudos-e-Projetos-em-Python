# Julia é professora e precisa de um programa para ajudar seus alunos a calcularem suas idades com base no ano de nascimento. 
# Sua tarefa é criar uma função que receba o ano de nascimento e o ano atual e retorne à idade correspondente.

def calculo_Idade(ano_Nasc, ano_Atual):
    return ano_Nasc - ano_Atual

ano_Nasc = int(input('Digite o seu ano de nascimento: '))
ano_Atual = int(input('Digite o ano atual: '))

idade = calculo_Idade(ano_Nasc, ano_Atual)
print(f'A sua idade é {idade}')
