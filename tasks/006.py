#6. Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

day = int(input('Введите число дня недели: '))
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
if day < 1 and day >7:
    day = int(input('Вы ввели что-то не то, в неделе 7 дней: '))

if day >= 1 and day < 6:
    day_week = week[day-1]
    print(f'{day_week} - working day')
elif day >5:
    day_week = week[day-1]
    print(f'{day_week} - day off')
        
        

#while day !=  range(1,8):


# # Дано число обозначающее день недели. Вывести его название и указать является ли он выходным. - сделано только на понедельник
# import os
# os.system("cls")

# week = ['понедельник', 'вторник', 'среда',
#         'четверг', 'пятница', 'суббота', 'воскресенье']
# n = input('Введите число, обозначающее день недели: ')
# while n != '1':
#     n = input(
#         'Ошибка, число должно быть в диапазоне от 1 до 7. \nВведите число, обозначающее день недели: ')
# else:
#     n = int(n)
#     print(f'Это', week[n-1], end=', ')
# if 1 <= n <= 5:
#     print('рабочий день!\n')
# else:
#     print('выходной день!\n')

# # обработка ошибок:

# def try_parse_int():
#     while True:
#         try:
#             console_input = int(input("Enter a weekday number: "))
#             return int(console_input)
#         except ValueError:
#             print("Is not a valid number.")
