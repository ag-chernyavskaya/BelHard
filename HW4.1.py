#Task4.1 v.1
password = input('Введите пароль')
up = False
sl = False
num = False
symb = False
symbol = '@#%&'
l = len(password)
if l <= 5:
    print(f'Введите пароль, состоящий минимум из шести символов')
else:
    for index in password:
        if index.isupper():
            up = True
        elif index.islower():
            sl = True
        elif index.isnumeric():
            num = True
        elif index in symbol:
            symb = True
    if up and sl and num and symb:
        print(f'Вы ввели хороший пароль')
    else:
        print(f'Попробуйте заново')

#Task_4.1 v.2
import re
p = input('Введите пароль')
d = len(p)
if d > 5 and re.search('[a-z]', p) and re.search('[A-Z]', p) and re.search('[\d]', p) and re.search('[@#%&]', p):
    print(f'Хороший пароль!')
else:
    print(f'Введите пароль заново')