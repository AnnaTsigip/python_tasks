 # Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

# list = []
# num=1
# product =1
# N = int(input('N = '))
# for i in range(1, N+1):
#     num = num *i
#     product = num
#     list.append(product)
# print(list)

'''

#Произведение:
# from math import prod

# n=int(input('Введите последнее число=')) 
# print(prod([i for i in range(1,n+1)]))
# #'Сумма чисел от 1 до, n, =, 
'''


from itertools import accumulate
import operator


n = int(input('n = '))

print(f'Набор произведений чисел от 1 до {n}: {list(accumulate([x for x in range(1, n + 1)], operator.mul))}')



