frase = "Rosas são vermelhas, violetas são azuis."

contagem_palavras = {}

for palavra in frase:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)