# Sara está participando de um concurso de escrita, e uma das regras exige que cada palavra de seu texto tenha um limite máximo de caracteres.

# Ajude Sara criando uma função que receba uma palavra e exiba a quantidade de caracteres.

def contagem_caracteres(palavra):
    return len(palavra)


texto = input('Digite a palavra: ')
print(f'Essa palavra tem {contagem_caracteres(texto)}')