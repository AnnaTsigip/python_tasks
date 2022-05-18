# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Пример:
# Входные данные:
#  'ываабв лповап абвцукв алоабвабв ываываыв'

# Входные данные: 
# 'лповап ываываыв'

# исходная строка
text = 'ываабв лповап абвцукв алоабвабв ываываыв'

# делим строку на слова
text_word = text.split()
#print(text_list)
# фрагмент, по которому будем удалять слова
find = 'абв'
# новый список для оставшихся слов
new_text = []
# проверяем, если в слове нет сочетания "абв" - добавляем его в новый список
for i in text_word:
    if find not in i:
        new_text.append(i)
           

print(new_text) # новый список
text_2 = ' '.join(new_text) # сбор новой строки через /join разделитель - пробел
print(text_2)

