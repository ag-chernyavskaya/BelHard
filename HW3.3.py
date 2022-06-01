#Task_3
year = int(input('Введите год: '))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f'Високосный год')
else:
    print(f'Не високосный год')
print(f'---------------------------')