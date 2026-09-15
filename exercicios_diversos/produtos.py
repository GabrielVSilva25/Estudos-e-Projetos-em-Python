prod1 = int(input('Digite o valor do 1° produto: R$ '))
prod2 = int(input('Digite o valor do 2° produto: R$ '))
prod3 = int(input('Digite o valor do 3° produto: R$ '))

if prod1 < prod2 and prod1 < prod3:
    print(f'O primeiro valor é o mais barato')

elif prod2 < prod1 and prod2 < prod3:
    print(f'O segundo valor é o mais barato')

elif prod3 < prod1 and prod3 < prod2:
    print(f'O terceiro valor é o mais barato')
