funcionario_1 = 1000
funcionario_2 = 770
funcionario_3 = 2700

bonus = 0.10

if funcionario_1 >= 1000:
    bonus_funcionario_1 = funcionario_1 * bonus
    print(f'O funcionario 1 teve {bonus_funcionario_1} bônus')

else:
    print(f'O funcionario 1 teve 0 bônus')


if funcionario_2 >= 1000:
    bonus_funcionario_2 = funcionario_2 * bonus
    print(f'O funcionario 2 teve {bonus_funcionario_2} bônus')

else:
    print(f'O funcionario 2 teve 0 bônus')


if funcionario_3 >= 1000:
    bonus_funcionario_3 = funcionario_3 * bonus
    print(f'O funcionario 3 teve {bonus_funcionario_3} bônus')

else:
    print(f'O funcionario 3 teve 0 bônus')
