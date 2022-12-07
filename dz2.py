# Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности
spisok = input("Задайте список чисел через пробел:   ").split()
def get_unique_numbers(numbers: list) -> list:
    unique = []
    for i in numbers:
        if i not in unique:
            unique.append(i)
    return unique
print(get_unique_numbers(spisok))  