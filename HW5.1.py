a = [35, 8, -20, 50, 4, 10, -5, 94, 7, 21]
max_element = max(a)
n = a.index(max_element)
new_a = a[:n + 2]
print(new_a)