# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


import random
k=int(input('k = '))

data = open('text_005.txt','a', encoding='utf-8')

for i in range(1, k+1):
    index = k
    k= k-1
    lst = random.randint(0,101)
    data.write(f'{lst}x^{index} + ')

data.write(f'{random.randint(0,100)} = 0\n') # добавляет свободный элемент
data.closed

'''
как убрать последний +

import random
k=int(input('k = '))
lstA = [random.randint(0,101) for item in range(k)] 

print(lstA)

lstB = []
for i in range(len(lstA)):
    #listB.append(str(listA[i]) + '*x**' + str(k-1) + ' + ')
    lstB.append(f'{str(lstA[i])}x^{str(k-1)} + ')
    k=k-1
print(lstB)

lstB.pop
#lstB.append(str(lstB[-1]))
lstB.append(' = 0')
text = ' '.join(lstB)
print(text)
#print(type(text))

with open('text_005.txt', 'a', encoding='utf-8') as r:
     r.write(text + '\n')
'''