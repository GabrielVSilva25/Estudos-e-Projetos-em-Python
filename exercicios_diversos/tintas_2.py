import math
metros_Quadrados = float(input('Informe o tamanho em m2 da área a ser pintada: '))

litros = metros_Quadrados / 6
total_litros = litros * 1.1

totalLatas18 = math.ceil(total_litros / 18)
litros_Restantes = total_litros - (totalLatas18 * 18)
    
totalLatas3_6 = math.ceil(litros_Restantes/ 3.6)

print(f'Serão necessárias x{totalLatas18} Latas de 18L e x{totalLatas3_6} galões de 3.6L')
print(f'O valor total: R${(totalLatas18*80) + (totalLatas3_6*25)}')
