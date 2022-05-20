# задать список из n чисел последовательности (1+〖1/n)〗^n и вывести на экран их сумму


# list = []
# N = int(input('N = '))
# for i in range(1, N+1):
#     num = (1+(1/i))**i
#     num_list = num
#     list.append(num_list)
#print(list)


n = int(input('Сколько элементов в последоватльности? \n'))
number = [1+(1/i)** i for i in range(1, n+1)]
print(f'Сумма {n} элементов последовательности = {round(sum(number),3)}')

