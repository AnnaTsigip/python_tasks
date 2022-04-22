# 14.Подсчитать сумму цифр в вещественном числе


num = float(input('numner = ')) # вводим число
num_str = str(float(num)) # переводим в строку
#print(type(num_str)) 
num_str1 = num_str.split('.') # разбиваем по разделителю
# print(num_str1)
num1 = int(num_str1[0]) # записываем до запятой
num2 = int(num_str1[-1]) # после запятой
#print(num1)
#print(num2)

def sum_num(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return(sum)

print(sum_num(num1) + sum_num(num2))
#print(sum_num(num2))

###########  2

# num = input("Введите число: ")
# sum = 0
# for i in range(0, len(num)):
#     if num[i] != ".":
#         sum += int(num[i])
# print(sum)

"""  3
# Подсчитать сумму цифр в вещественном числе.
import os
import random
os.system("cls")

# задаем случайное вещественное число из диапазона
a = random.uniform(1, 1001)
print('Задано число:', a)

a = str(a).replace('.', '')     # переводим в строковый тип, убираем точку
print(a)
p=list(map(int,a))
summa = sum(p)        # переводим в числовой тип, считаем сумму
print('Сумма цифр данного числа равна:', summa, '\n')



"""
#4

string_number = str(float(input('Enter a real number: '))).replace('.', '')
list_number = [int(a) for a in string_number]
print(f'Sum of all digits in the real number is {sum(list_number)}.')
