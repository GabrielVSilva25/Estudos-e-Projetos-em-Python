
numeros = ('um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze', 'catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    num = int(input('Digite um número de 1 a 20: '))

    if 0 <= num <=20:
        break
    print('tente novamente. ')
    
print(f'Você digitou o número {numeros[num]}')