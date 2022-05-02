# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


#как убрать последний +

import random
k=int(input('k = '))
listA = [random.randint(1,100) for item in range(k)] 

print(listA)

listB = []
for i in range(len(listA)):
    #listB.append(str(listA[i]) + '*x**' + str(k-1) + ' + ')
    listB.append(f'{str(listA[i])}x**{str(k-1)} + ')
    k=k-1
print(listB)

listB.append(str(' = 0'))
text = ''.join(listB)
print(text)



with open('text_005.txt', 'a', encoding='utf-8') as r:
     r.write(text + '\n')



