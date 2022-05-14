# 35. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
#  a открытие для добавления данных
#  r открытие для чтения данных
#  w открытие для записи данных
#  w+ r+ 

with open('file_35.txt', 'w') as data:
    data.write('0 1 2 3 4 5 6 7 8 9 11')
    
with open('file_35.txt', 'r') as data:
    numbers = data.readline()
print(numbers)
#print(type(numbers)) <class 'str'>

numbers2 = numbers.split()
#print(type(numbers2)) <class 'list'>

for i in range(0, len(numbers2)):
    if int(numbers2[i]) +1 != i + 1:
        find = i
        break
print(find)
