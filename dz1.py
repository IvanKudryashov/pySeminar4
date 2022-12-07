# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
n = int(input('Введите число: '))
def funk(num: int) -> list:
    i = 2
    f = []
    while i <= num:
        if  not num % i:
            if not f.count(i):
                f.append(i)
            num //= i
        else:   
            i += 1
    return f
print(funk(n))            