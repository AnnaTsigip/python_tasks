# 26. Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. 
#  Т е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

#функция факториал
# import math
# a = math.factorial(5)
# print(a)



num = int(input('Введите числло: '))
fib1=1
list = [0]
for i in range(0,num):
    fib2=list[i]
    #sum = fib1+fib2
    list.append(fib1+fib2)    
    fib1=fib2
    #fib2=sum
    #list.append(sum)
print(list)

list2 = []
d=1
for i in range(1, num+1):
    list2.insert(0,list[i] * d)
    d*=-1  

list3 = [list2 + list]
print(list3)


'''

# поиск эдемента последовательности: 
prew = cur = 1
element = input('Введите номер искомого элемента : ')
element = int(element)
for n in range(int(element-2)):
    tmp = prew + cur
    prew = cur
    cur = tmp
    #print(tmp)
print(str(element)+' элемент последовательности равен ' + str(cur)) # 8 элемент последовательности равен 21


'''
# # выводятся сразу все элементы:
# def fibonacci(n):
#     a, b = 1, 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b

# # data = list(fibonacci(10))
# # print(data)
# print(list(fibonacci(10)))

# # элементы выводятся по одному:

# def fibonacci():
#     a, b = 1, 1
#     while True:
#         yield a
#         a, b = b, a + b

# gen = fibonacci()
# for i in range(5):
#     print(next(gen))
