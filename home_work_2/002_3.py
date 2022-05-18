# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: 
# На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 

# b) Подумайте, как наделить бота "интеллектом"



candies = int(input('Сколько конфет: '))
take = int(input("Максимальное количество конфет можно взять: "))
# сколько нужно взять конфет для победы: 
def take_to_have_for_first(candies, take):
     take_candies = candies % (take + 1)
     if take_candies == 0:
         take_candies = take
     return take_candies


count = 0
while candies > 0:
    count += 1
    player = int(input("Ход первого игрока. Возьмите конфеты: "))
    candies = candies - player
    if candies > 0:
        bot = take_to_have_for_first(candies, take)
        print(f'bot взял {bot} конфет')
        candies = candies - int(bot)
        print(f'осталось конфет: {candies}')
        #print(take_to_have_for_first(candies, take))
if candies == 0:
    print('Игра окончена')
if count % 2 == 0:
    print(f'Победил игрок player')
else:
    print(f'Победил игрок bot')



# # бот ходит первым
# candies = int(input('Сколько конфет: '))
# take = int(input("Максимальное количество конфет можно взять: "))

# # сколько нужно взять конфет для победы: 
# def take_to_have_for_first(candies, take):
#      take_candies = candies % (take + 1)
#      return take_candies

# count = 0

# while candies > 0:
#     count += 1
#     bot = take_to_have_for_first(candies, take)
#     print(f'bot взял {bot} конфет')
#     candies = candies - int(bot)
#     if candies > 0:
#         player = int(input("Ход игрока. Возьмите конфеты: "))
#         candies = candies - player
#         print(f'осталось конфет: {candies}')
#         #print(take_to_have_for_first(candies, take))

# if candies == 0:
#     print('Игра окончена')
# if count % 2 == 0:
#     print(f'Победил игрок bot')
# else:
#     print(f'Победил игрок player')