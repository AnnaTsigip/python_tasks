# 10. Найти расстояние между тремя точками пространства

import os
os.system('cls')

print('Введите координаты точки A: ')
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))
z1 = float(input('z1 = '))
print('Введите координаты точки B:')
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))
z2 = float(input('z2 = '))

AB = round(((x2-x1)**2 + (y2-y1)**2 + (z2 - z1)**2)**0.5, 2)
print(f'Расстояние между точками A и B = {AB}')