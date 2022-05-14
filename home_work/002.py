#2. Задайте натуральное число N.
#  Напишите программу, которая составит список простых множителей числа N

def Factor(N):
    multipliers = []
    n = 2
    while n * n <= N:
        if N % n == 0:
            multipliers.append(n)
            N //= n
        else:
            n += 1
    if N > 1:
        multipliers.append(N)
    return multipliers

print(Factor(58984))


"""
N = int(input("Введите натуральное число N:\n"))
List = []
for i in range(2, N):
while N % i == 0:
List.append(i)
N = N/i
if N == 1:
break

if len(List) == 0:
print("Число является простым")
else:
print("Cписок множителей числа N:")
print(List)
"""
