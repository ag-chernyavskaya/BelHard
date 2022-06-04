st = input('Введите предложение: ')
sp = list(st)
l = len(sp)
print(sp)
print(l)
for i in range(l):
    if sp[i] == '(':
         a = i
for j in range(l):
    if sp[j] == ')':
         b = j
print(f'Символы внутри скобок: {" ".join(sp[a+1:b])}')