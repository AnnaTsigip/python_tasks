#Сформировать список из  N членов последовательности.
#Для N = 5: 1, -3, 9, -27, 81 и т.д.

list = []
N = int(input('Введите количество членов последовательности: '))
for i in range(N):
    if i % 2 == 0:
        list.append(3**i)
    else:
        list.append(-3**i)
print(list)


#2

import os
os.system("cls")

def sub (x):
    if x in [0,1]:
        return 1
    else:
        return sub (x-1)*-3
list = []
for N in range (1,10):
    list.append (sub(N)) # Добавление элемента в конец списка
print (list)


#3
count = int(input('Введите количество элементов: '))
num = 1
list = [1]

for i in range (0, count - 1):
    num *= -3
    list.append(num)

print(list)


#4
n = int(input('Введите число: '))
 
def get_degree(n):
    return[((-3)**i) for i in range(n)]
 
print (get_degree(n))



#5

def power(s):
    """
    Function will get power of number -3
    """
    new = (-3) ** s

    return new

n = 20
spisok=[]

for i in range(n):
    spisok.append(power(i))

print(f"List of elements: {spisok}")
