# 13) Em uma empresa de venda de imóveis você precisa criar um código que analise os dados de vendas anuais para ajudar a diretoria na tomada de decisão. O código precisa coletar os dados de quantidade de venda durante os anos de 2022 e 2023 e fazer um cálculo de variação percentual. A partir do valor da variação, deve ser enviada às seguintes sugestões:

# Para variação acima de 20%: bonificação para o time de vendas.
# Para variação entre 2% e 20%: pequena bonificação para time de vendas.
# Para variação entre 2% e -10%: planejamento de políticas de incentivo às vendas.
# Para variação abaixo de -10%: corte de gastos.


vendas_2022 = int(input("Digite o total de vendas de imóveis em 2022: "))
vendas_2023 = int(input("Digite o total de vendas de imóveis em 2023: "))


if vendas_2022 == 0:
    if vendas_2023 > 0:
        variacao_percentual = float('inf')
    else:
        variacao_percentual = 0

    variacao_percentual = ((vendas_2023 - vendas_2022) / vendas_2022) * 100

print(f"\n Vendas em 2022: {vendas_2022}")
print(f"Vendas em 2023: {vendas_2023}")
print(f"Variação Percentual: {variacao_percentual:.2f}%")


print("\n Sugestões para a Diretoria:")

if variacao_percentual > 20:
    print("Acima de 20%: Bonificação para o time de vendas (Grande Incentivo).")
elif 2 <= variacao_percentual <= 20:
    print("Entre 2% e 20%: Pequena bonificação para o time de vendas (Incentivo Moderado).")
elif -10 <= variacao_percentual < 2:
    print("Entre 2% e -10%: Planejamento de políticas de incentivo às vendas (Ação Estratégica).")
else:
    print("Abaixo de -10%: Corte de gastos e revisão de estratégias (Ação Urgente).")

