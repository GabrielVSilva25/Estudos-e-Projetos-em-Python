meta_funcionario = 10000
meta_loja = 300000

vendas_funcionario = 10001
vendas_loja = 300001

nota_Func = 9

if nota_Func >= 9 or vendas_funcionario >= meta_funcionario and vendas_loja >= meta_loja:
    bonusFuncionario = vendas_funcionario * 0.03
    print(f'O Funcionario rebeceu mais {bonusFuncionario} bônus.')

else:
    print('Não foi obtido bônus.')