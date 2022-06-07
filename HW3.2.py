#Task_2
a = float(input('Введите число:'))
b = float(input('Введите число:'))
c = float(input('Введите число:'))
sum = a + b + c
min_number = min(a, b, c)
print(f'Минимальное значение {min_number}')
max_number = max(a, b, c)
print(f'Максимальное значение {max_number}')
sr = sum - min_number - max_number
print(f'Среднее значение {sr}')
if min_number > 1 and min_number % 2 == 0:
    print(f'{min_number}')
else:
    print(f'Число меньше единицы или нечетное')
if max_number > (sr + min_number) / 2 or max_number < sr * min_number:
    print(f'{max_number}')
else:
    print(f'Введите другое число')
if sr % 3 == 0 and sr % 2 == 0:
    print(f'{sr}')
else:
    print(f'Введите другое число')
print(f'---------------------------')