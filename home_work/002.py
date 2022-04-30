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

print(Factor(180))
