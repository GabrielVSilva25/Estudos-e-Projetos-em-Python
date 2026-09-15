cpf = input('Informe o CPF: ')

if cpf.isdigit():
    if len(cpf) != 11:
        print('Erro: O CPF deve conter exatamente 11 dígitos.')

    else:
        print('CPF válido.')
else:
    print('Erro: O CPF deve conter apenas números.')
