# 006/ 34 Даны два файла в каждом из которых находится запись многочлена. 
# Сформировать файл содержащий сумму многочленов.

# import random
# k=int(input('k = '))

# data = open('text_005.txt','a', encoding='utf-8')

# for i in range(1, k+1):
#     index = k
#     k= k-1
#     lst = random.randint(0,101)
#     data.write(f'{lst}x^{index} + ')

# data.write(f'{random.randint(0,100)} = 0\n') # добавляет свободный элемент
# data.closed



with open('text_006_1.txt', 'r', encoding='utf-8') as r:
    pol_1 = r.readlines()
    print(pol_1)
    #print(type(pol_1))


with open('text_006_2.txt', 'r', encoding='utf-8') as r:
    pol_2 = r.readlines()
    #print(pol_2)

pol_1new = str(pol_1)
pol_1new = pol_1new.replace(' = 0', '')
pol_1new = pol_1new.split('+')
print(pol_1new)
pol_2new = str(pol_2)
pol_2new = pol_2new.replace(' = 0', '')
pol_2new = pol_2new.split('+')
print(pol_2new)

for i in range(len(pol_1new)):
    sym = (f'({(pol_1new[0])} + {(pol_2new[0])} )+ ({(pol_1new[1])} + {(pol_2new[1] )})+ ({(pol_1new[2])} + {(pol_2new[2] )})+({(pol_1new[3])} + {(pol_2new[3])})' )
print(sym)



with open('text_006.txt', 'a', encoding='utf-8') as r:
     r.write(sym + '\n')