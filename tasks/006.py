#6. Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

day = int(input('Введите число дня недели: '))
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
if day > 7:
    print("В нелеле всего 7 дней")

elif day >= 1 and day < 6:
    day_week = week[day-1]
    print(f'{day_week} - working day')
elif day >5:
    day_week = week[day-1]
    print(f'{day_week} - day off')
        
        

