meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]

vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

lista_faturamento = vendas_1sem + vendas_2sem

maior_faturamento = max(lista_faturamento)
menor_faturamento = min(lista_faturamento)

mes_maiorfaturamento = lista_faturamento.index(maior_faturamento)
mes_menorfaturamento = lista_faturamento.index(menor_faturamento)

print(f'o melhor faturamento foi no mês de {meses[mes_maiorfaturamento]} com {maior_faturamento} vendas ')
print(f'o pior faturamento foi no mês de {meses[mes_menorfaturamento]} com {menor_faturamento} vendas ')
