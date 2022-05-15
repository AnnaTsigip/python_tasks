# 3 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример:
# На сжатие:
# Входные данные:
# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Входные данные: 
# 12W1B12W3B24W1B14W


#date = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
# count = 1
# s = []
# for i in range(len(date)):
#     if date[i] != date[i+1]:
#         s.append(1*[i])
#     elif date[i] == date[i+1]:
#         count +=1
#     s.append(count * [i])
# print(s)


with open('file_003.txt', 'w') as data:
    data.write('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')
    
with open('file_003.txt', 'r') as data:
    string = data.readline()

#string = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
cout = 1
for i in range(len(string)-1):
    if i <= len(string):
        if string[i] == string[i + 1]:
            cout += 1
        else:
            a = string[i]
            print(cout, string[i], end=' ')
            cout = 1

print(cout, string[i], end=' ')

#как перевести чтоб сохранить в файл
# with open('file_003_2.txt', 'w') as data:
#     data.write(cout, string[i])

    

