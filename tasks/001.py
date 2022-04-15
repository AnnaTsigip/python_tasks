# 1. По двум заданным числам проверить является ли одно квадратом второго 

import os # для очистки консоли
os.system('cls')


first_number = int(input('Первое число: '))
second_number = int(input('Второе число: '))
if second_number == first_number**2:
    print(f'{second_number} является квадратом {first_number}')
elif first_number == second_number**2:
    print(f'{first_number} является квадратом {second_number}')
else:
    print(f'числа НЕ является квадратом друг друга')