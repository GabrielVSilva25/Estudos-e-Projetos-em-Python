# Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. Se algum valor for negativo, mostre uma mensagem informando o erro.

atv1 = int(input('Informe a quantidade de dias para a atividade 1: '))
atv2 = int(input('Informe a quantidade de dias para a atividade 2: '))
atv3 = int(input('Informe a quantidade de dias para a atividade 3: '))

if atv1 >= 0 and atv2 >= 0 and atv3 >= 0:
   tempo_total_atividades = atv1 + atv3 + atv2

   print(f'A quantidade de tempo total é de {tempo_total_atividades} dias')

else:
   print('Foi informado um valor negativo, tente novamente.')
