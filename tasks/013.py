# 13. Пользователь задаёт две строки. Определить количество вхождений одной строки в другой 
# sub – это подстрока для поиска.
# start – поиск начинается с этого индекса. Первый символ начинается с 0 индекса. По умолчанию поиск начинается с 0 индекса.
# end – поиск заканчивается на этом индексе. Первый символ начинается с 0 индекса. По умолчанию поиск заканчивается на последнем индексе.
# str.count(sub, start = 0,end = len(string))

text = 'Лучше знать немного истинно хорошего и нужного, чем очень много посредственного и ненужного'
count = 0
for i in text:
    if i == 'о':
        count = count + 1
print(count)


#2

# используя метод .count()
# sub = 'о'
# print ("text.count('о') : ", text.count(sub))


#3

from itertools import count
import os
os.system('cls')

str1 = '''Один из наиболее известных русских писателей и мыслителей, 
            один из величайших писателей-романистов мира. Участник обороны Севастополя. 
            Просветитель, публицист, религиозный мыслитель, его авторитетное мнение 
            послужило причиной возникновения нового религиозно-нравственного течения - толстовства. 
            За свои взгляды был отлучён от РПЦ. Член-корреспондент Императорской Академии наук, 
            почётный академик по разряду изящной словесности. Был номинирован на 
            Нобелевскую премию по литературе. Впоследствии отказался от дальнейших номинаций. 
            Классик мировой литературы.'''
str2 = 'из'


print('Количество вхождений второй строки в первую: ',
      str1.count(str2), '\n')


# 4
text_1 = input('Введите первую строку' + '\n')
text_2 = input('Введите вторую строку' + '\n')
count = 0
for i in text_1:
    for j in text_2:
        if [j] == [i]:
            count += 1
print(f'Количество совпадений символов в первой и во второй строке = {count}')


#5
def text_find(a,b):
    """
    Function will find occurence of word in the text
    """
    count = 0
    i = 0
    while i <= len(a):
        if b in a[i: i+len(b)]:
            #print("Найдено повторение номер", count+1)
            count += 1
            i += len(b)
        else:
            i += 1
    return count

a = "a тесты тесты тессс тесты"
b = "тесты"

print(f"Count of first word in second phrase: {text_find(a,b)}")
print(f"Count of first word in second phrase: {text_find('аааааааааа','аа')}")



#6


# str1= input('First string: ')
# str2= input('Second string: ')

str1 = 'Python free 777 $$$ python free python python python $$$ python'
str2 = 'python free new $$$'

str_list = str1.lower().split()
substr_list = str2.lower().split()

counter = {}
for substr_element in substr_list:
    substr = substr_element
    for str_element in str_list:
        if str_element == substr:
            counter[str_element] = counter.get(str_element, 0) + 1

same_words = {element: count for element, count in counter.items() if count > 0}

print('String: ' + str1)
print('Substrings: ' + str2)
print()
print(same_words)

