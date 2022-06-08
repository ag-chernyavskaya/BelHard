b = [35, 8, -20, 50, 4, 10, -5, 94, 7, 21]
b_max = max(b)
b_min = min(b)
n_max = b.index(b_max)
n_min = b.index(b_min)
if n_max > n_min:
    b_1 = b[:n_min + 1]
    b_2 = b[n_max:]
    b_new = b_1 + b_2
else:
    b_1 = b[:n_max + 1]
    b_2 = b[n_min:]
    b_new = b_1 + b_2
print(b_new)