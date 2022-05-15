# # 2/2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: 
# На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# a) Добавьте игру против бота


from random import randint

candies = int(input('Сколько конфет: '))
take = int(input("Максимальное количество конфет можно взять: "))

# сколько нужно взять конфет для победы: 
def take_to_have_for_first(candies, take):
     take_candies = candies % (take + 1)
     return(f'чтобы выиграть первому ходящему необходимо взять {take_candies}')

count = 0

while candies > take:
    count += 1
    player = int(input("Ход первого игрока. Возьмите конфеты: "))
    candies = candies - player
    bot = int(randint(1,take))
    print(f'bot взял {bot} конфет')
    candies = candies - bot
    print(f'осталось конфет: {candies}')
    #print(take_to_have_for_first(candies, take))
if candies < take:
    print('Игра окончена')
if take % 2 != 0:
    print(f'Победил игрок player')
else:
    print(f'Победил игрок bot')