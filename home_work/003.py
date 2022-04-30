#3. Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random

spisok =[]
a = int(input("Введите длину списка :"))
for i in range(a):
    spisok.append(random.randint(1,10))
print(f"Создан новый список: \n {spisok}")

unique_numbers = set(spisok) # переводим в множество, дубли удаляются

list_of_unique_numbers = [] # пустой список, для множества
for number in unique_numbers: # переводим множество в список 
    list_of_unique_numbers.append(number)
print(list_of_unique_numbers)