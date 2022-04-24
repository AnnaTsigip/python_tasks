# 18. Реализовать алгоритм перемешивания списка. 

'''
через рандом: 


import random


listA = [2, 8, 4, 31, 1, 15] 
random.shuffle(listA)
print(listA)


'''
import random

list = []
N = int(input('N = '))
for i in range(-N, N+1):
    list.append(i)
#print(list)

for i in range(len(list)):
    j = random.randint(-N, N)
    list[i], list[j] = list[j], list[i]
print(list)