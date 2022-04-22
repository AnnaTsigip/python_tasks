# задать список из n чисел последовательности (1+〖1/n)〗^n и вывести на экран их сумму

#1
list = []
N = int(input('N = '))
for i in range(1, N+1):
    num = (1+(1/i))**i
    num_list = num
    list.append(num_list)

print(list)



def list_sum(listsum):
    sum =0
    for i in list:
        sum = sum + i
    return sum

print(list_sum(list))


#2 
# def listsum(numList):
#     theSum = 0
#     for i in numList:
#         theSum = theSum + i
#     return theSum

# print(listsum([2.0, 2.25, 2.37037037037037, 2.44140625]))



"""  3
import os
import random
os.system("cls")

n = random.randint(6, 16)
print(n)

massive = []

for i in range(1, n+1):
    massive.append(1+(1/i)**i)
print(f'{sum(massive):.2f}')

"""