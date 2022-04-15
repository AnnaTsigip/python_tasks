# 2. Найти максимальное из пяти чисел
"""
list = [5, 7, 12, 6, 1]
print(max(list))
"""



a = int(input('Введите a: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))
d = int(input('Введите d: '))
e = int(input('Введите e: '))
max = a
if b > max:
    max =b
if c > max:
    max = c
if d > max:
    max = d
if e > max:
    max = e
print(f'максимальное число = {max}')
