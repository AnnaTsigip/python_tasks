
#Сформировать список из  N членов последовательности.
#Для N = 5: 1, -3, 9, -27, 81 и т.д.


# list = []
# N = int(input('Введите количество членов последовательности: '))
# for i in range(N):
#     if i % 2 == 0:
#         list.append(3**i)
#     else:
#         list.append(-3**i)
# print(list)

N = int(input('Введите количество членов последовательности: '))
list = [(3**i) if i % 2 == 0 else (-3**i) for i in range(N) ]

print(list)
