
# Вычислить число c заданной точностью d
# Пример:
# при d=0.001, p=3.141,  10**-1<=d<=10**-10 


p = '3.1415926535'
d=float(input('d = '))
d = str(d)
d=abs(d.find('.') - len(d)) - 1
print(p[0:d+2])
