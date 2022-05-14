#32. Задайте последовательность чисел. 
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


"""
вариант 2
subs = [1, 3, 5, 4, 9, 14, 5, 1]
alone = []
for i in range (0, len(subs)):
duplicate = 0
for j in range(0, len(subs)):
if i != j:
if subs[i] == subs[j]:
duplicate = 1
if duplicate == 0:
alone.append(subs[i])
print(alone)
"""

# вариант3 
# numbers=list(map(int,input('Введите последовательность чисел через пробел: ').split()))

# print("Cписок неповторяющихся элементов исходной последовательности: ", list(set(numbers)))