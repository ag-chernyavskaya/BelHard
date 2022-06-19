def func(*args):
    n_2 = 0
    n_3 = 0
    def number(numb):
        return len(str(numb))
    for i in args:
        if number(i) == 2:
            n_2 += 1
        elif number(i) == 3:
            n_3 += 1
    return f' Количество двухзначных чисел: {n_2}\n Количество трехзначных чисел: {n_3}'
print(func(123, 2424, 424, 22, 59, 158, 7894))

