
#30. Вычислить число c заданной точностью d
# Пример:
# при d=0.001, p=3.141,  10**-1<=d<=10**-10 


p = '3.1415926535'
d=float(input('d = '))
d = str(d)
d=abs(d.find('.') - len(d)) - 1
print(p[0:d+2])

'''
import math
P = 0.001
#P = float(input("Введите количество знаков после запятой для вычисления числа Пи (от 1 до 10 ):\n"))
P = str(P).split('.')
L = len(P[1])
M = str(math.pi)
print(float(M[:L+2]))
'''