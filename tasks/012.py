#12. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
#Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


slovar = {}
n = int(input('n = '))
for i in range(1,n+1):
    slovar[i] = 3*i+1
print(slovar)


#2
import os
#from typing import Dict
os.system("cls")


Dictionary = {n:3*n+1 for n in range (1,7)}
print (Dictionary)


#3
# from random import randint
# def get_dict(n):
#     return {x: 3 * x + 1 for x in range(1, n + 1)}
# n = randint(1, 20)
# print(n)
# print(get_dict(n))
