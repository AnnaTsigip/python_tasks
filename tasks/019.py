#19. Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел

"""

Возвращаемое значение:
функция time.time() - float,
функция time.time_ns() - int.

#local = time.ctime(start_time) # показывает текущую дату
"""

# с генератором 
# from random import randrange

# n = 10
# a = [randrange(1, 10) for i in range(n)]
# print()

#без генератора, с использованием времени

import time

#second = time.time()
second = time.time()
num = str(second)
# num = float(result[:6:-1])/1000
# num = int(result[-4:]) // 100
# num2 = int(num)//1000
n = num.split('.')
result = n[1]
print(num)
print(result)
#print(num)




# def rand_numbers(start, stop):
#     num = time.time() # проверить
#     delta = stop - start
#     rnd = float(str(num)[::-1][:3])/1000
#     return round(rnd * delta)

# print(rand_numbers(1, 30))


# num = 1648892099.8172002
# rnd = float(str(num)[::-1][:4])
# print(num)
# print(rnd)