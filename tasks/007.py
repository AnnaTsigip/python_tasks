# 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

x = [True, False]
y = [True, False]
z = [True, False]
for i in x:
    for j in y:
        for k in z:
            print('Для x:', x[i])
            print('Для y:', y[j])
            print('Для z:', z[k])
            if (not(x[i] or y[j] or [k]) == (not x[i] and not y[j] and not z[k])):
                print(' Выражение истинно')
            else: 
                print(' Выражение ложно')




# 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
from unittest import result


def logic(x, y, z):
    if (not (x or y or z) == (not x and not y and not z)):
        result = True
    else:
        result = False
    print(result)
    return result

f1 = logic(True, True, True)
f2 = logic(True, True, False)
f3 = logic(True, False, True)
f4 = logic(False, True, True)
f5 = logic(True, False, False)
f6 = logic(False, False, True)
f7 = logic(False, True, True)
f8 = logic(False, False, False)

if (all([f1, f2, f3, f4, f5, f6, f7, f8])) == True:
    print('Выражение тождественно')
else:
    print('Выражение НЕ тождественно')



#Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

x = [True, False]
y = [True, False]
z = [True, False]
check = 1

for i in range (0, 2):
    for j in range (0, 2):
        for k in range (0, 2):
            if (not (x[i] or y[j] or z[k]) == (not x[i] and not y[j] and not z[k])):
                print(f'Выражение из условия - True')
            else:
                print(f'Выражение из условия - False')
                check = 0

if (check == 1):
    print('Выражение ИСТИННО!')
else:
    print('Выражение ЛОЖНО!')



# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

import os
os.system("cls")

x = [True, False]
y = [True, False]
z = [True, False]
print('\tX\tY\tZ\t¬(X ⋁ Y ⋁ Z)\t¬X ⋀ ¬Y ⋀ ¬Z\t¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
print('_'*100)
for index in range(2):
    for count in range(2):
        for i in range(2):
            left = not(x[index] and y[count] and z[i])  # левая часть равенства
            print(f"\t{x[index]} \t{y[count]} \t{z[i]}\t\t{left}", end='')
            right = not(x[index]) or not(y[count]) or not(
                z[i])  # правая часть равенства
            print(f"\t\t{right}", end='')
            print('\t\t', left == right)
print('\n')

# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
a = [0, 1]
print('X Y Z F')
for x in a:
    for y in a:
        for z in a:
           f = not(x or y or z) == (not x and not y and not z)
           print (x, y, z, int(f))
