# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

usuario = 'nome'
senha = 123

login = input('Informe o usuário: ')
password = input('Informe a senha')

if login == usuario and password == senha:
    print('Login realizado com sucesso.')

else:
    print("Credenciais inválidas. Tente novamente.")