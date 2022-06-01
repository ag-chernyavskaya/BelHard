#Task_1
a = float(input('Введите число:'))
b = float(input('Введите число:'))
c = float(input('Введите число:'))
if a + b <= c or a + c <= b or b + c <= a:
    print(f'Треугольник не существует')
else:
    print (f'Треугольник существует')
    if a == b == c:
        print(f'Треугольник равносторонний')
    elif a == b or a == c or b == c:
        print(f'Треугольник равнобедренный')
    else:
        print(f'Треугольник разносторонний')
print(f'----------------------------')