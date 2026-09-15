frase = str(input('Digite uma frase: ')).lower().strip()

vezes = frase.count('a')
esq = frase.find('a')
dir = frase.rfind('a')
print(f'A letra A aparece {vezes} na frase.')
print(f'A primeira A aparece na posição{esq+1}')
print(f'A última letra A aparece na posição {dir+1}')

