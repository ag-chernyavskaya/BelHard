#Task_4
age = float(input('Введите свой возраст: '))
weight = float(input('Введите свой вес (в килограммах): '))
height = float(input('Введиме свой рост (в метрах): '))
I = weight / height ** 2
print(f'Возраст: {age} Вес: {weight} Рост: {height}')
print(f'Индекс массы тела: {I}')
if age < 45:
    if I < 18.5:
        print(f'Недостаточная масса тела')
    elif I >= 18.5 and I <= 24.99:
        print(f'Норма')
    elif I >= 25 and I <= 29.99:
        print(f'Избыточная масса тела')
    elif I >= 30:
        print(f'Ожирение')
else:
    if I < 22:
        print(f'Недостаточная масса тела')
    elif I >= 22 and I <= 26.99:
        print(f'Норма')
    elif I >= 27 and I <= 31.99:
        print(f'Избыточная масса тела')
    elif I >= 32:
        print(f'Ожирение')