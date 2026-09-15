tamanho = float(input('Qual o tamanho do arquivo de download? (MB) '))
velocidade = int(input('Qual a velocidade da internet? (Mbps) '))

tempo_download = (tamanho / velocidade) * 60

print(f'O tempo estimado para o download é de {tempo_download} minutos.')