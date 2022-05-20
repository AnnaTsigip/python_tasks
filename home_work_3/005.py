# задать список из n чисел последовательности (1+〖1/n)〗^n и вывести на экран их сумму

import os
import random
os.system("cls")

n = random.randint(6, 16)

num = [1+(1/i)**i for i in range(1, n+1)]
print('Задана последовательность из ', n,
      'чисел:\n', *num, '\nСумма чисел = ', round(sum(num), 2), '\n')



# 17. Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

N = int(input('Введите число' + '\n'))
list = [i for i in range(-N,N+1)]
path = '17.txt'
data = open(path,'r')
count = 1
for line in data:
    if int(line) > len(list)-1:
        count*=1
    else:    
        count *= list[int(line)]
print(count)
data.close()




