# 4. Показать первую цифру дробной части числа


# через строку 

number = float(input('Введите число: '))
number1=str(float(number)) # перевод числа в строку
number2 = number1.split('.') # разбиваем по "."
#print(number2) 
#print(type(number1))
number3 = number2[1] # берем цифру после точки
#print(number3)
number_fin =number3[0] # распечатываем первую цифру
print((number_fin))


#математически:
n = float(input('n = '))
num = int(n*10)%10
print(f'Первая цифра дробной части числа {n} - {num}')