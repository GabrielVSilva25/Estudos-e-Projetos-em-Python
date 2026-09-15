cpf = input('Informe seu CPF: ')

cpf = cpf.strip()
cpf = cpf.replace('.', '')
cpf = cpf.replace('-', '')


if len(cpf) == 11 and cpf.isnumeric():
    print(cpf)

else:
    print('Digite o cpf corretamente e apenas os números')
