lista_nomes = []
lista_idades = []

def menu():
    opcao = int(input('''

    MENU

    1 - Cadastrar pessoa
    2 - Listar pessoas
    3 - Buscar pessoa
    4 - Quantidade de pessoas
    5 - Sair

    Qual opcão deseja: '''))

    return opcao

def cadastrar():

    print('=== Cadastro de pessoas ===')
                
    nome = input('Qual o seu nome: ')
    lista_nomes.append(nome)

    idade = int(input('Qual a sua idade: '))
    lista_idades.append(idade)


def listar_pessoa():

    for i in range(len(lista_nomes)): 
        print(f'{lista_nomes[i]} - {lista_idades[i]}')

def buscar_pessoa():
    
    buscar_nome  = input('Qual nome deseja pesquisar? ')

    for nome in lista_nomes:
        if buscar_nome == nome:
            pegarindice = lista_nomes.index(nome)
            print(f'Encontrado - {lista_nomes[pegarindice]}, {lista_idades[pegarindice]}')
            break

    else:
        print(f'O nome {buscar_nome} não foi encontrado.')

def qtd_pessoas():

    qtd_cadastrados = len(lista_nomes)
    print(f'Temos {qtd_cadastrados} pessoa(s) na lista.')
    
opcoes = menu()

while opcoes != 5:
    if opcoes == 1:
        cadastrar()

    elif opcoes == 2:
        listar_pessoa()
  
    elif opcoes == 3:
        buscar_pessoa()

    elif opcoes == 4:
        qtd_pessoas()

    else:
        pass
    opcoes = menu()