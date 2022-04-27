#17 Задать список из N элементов, заполненных числами из [-N, N].
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число

"""
ввести список с клавиатуры:
a=[int(i) for i in input().stlit]
список аналогичный a:
b=[item for item in a]
"""
N = int(input('N = ')) # определяем N
lis_N = [] # создаем список 
prod = 1
f = open('file_17.txt', 'r')
f.close

for i in range(-N, N+1):
    lis_N.append(i)
print(lis_N)

for line in f:
    prod = prod * int(lis_N[int(line)]) # 
print(prod)

# читаем информацию из файла
# r=open('file_17.txt', 'r')
# for line in r:
#     print(line, end="")
# r.close


