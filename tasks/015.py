# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]


# вводим число
# от 1 до n=count*i


list = []
num=1
product =1
N = int(input('N = '))
for i in range(1, N+1):
    num = num *i
    product = num
    list.append(product)
print(list)


#2
# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]
import os
import random
os.system("cls")

n = random.randint(6, 16)
print(n)

list = [1]

for i in range(2, n+1):
    list.append(i * list[i-2])

print(list, '\n')
