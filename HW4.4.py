st = input('Введите строку с точкой: ')
new_st = ''
l = len(st)
for i in st:
    if i != '.':
        new_st += i
    elif i == '.':
        break
n = len(new_st.split(' '))
print(f'Количество слов в строке: {n}')