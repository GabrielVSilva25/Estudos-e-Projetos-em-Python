# Beatriz está desenvolvendo um sistema de atendimento para um site de serviços. Ela deseja criar um programa que exiba uma saudação personalizada dependendo da hora do dia que o usuário acessa a plataforma. 
# O sistema deverá ter a seguinte regra:

# Se for antes das 12h, exibir "Bom dia";

# Entre 12h e 18h, exibir "Boa tarde";

# Após 18h, exibir "Boa noite".

def saudacao(horario):
    if horario < 12:
        return 'Bom dia'

    elif horario >= 12 and horario < 18:
        return 'Boa tarde'
    
    else:
        return 'Boa noite'


horario = int(input('Informe o horario: '))
print(saudacao(horario))
