# Um instituto de meteorologia deseja fazer um estudo de temperatura média de cada mês do ano. 
# Para isso, você precisa fazer um código que colete e armazene essas temperaturas médias em uma lista. 
# Depois, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual e em que mês elas ocorreram, 
# mostrando os meses por extenso (Janeiro, Fevereiro, etc.).

temperatura = []
meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
maior = []

for i in range(0, 12):
    temperatura.append(int(input(f'Informe a temperatura do mês de {meses[i]}: ')))

media = sum(temperatura) / len(meses)

for i in range(0, 12):
    if temperatura[i] > media:
        maior.append(meses[i])


print(f'Os meses que tiveram temperatura acima da média foram: {maior}')

