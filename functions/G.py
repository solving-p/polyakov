def fisich_n_fibb(x):
    a, b = 1, 1
    if x == 1 or x == 2:
        return 1
    for i in range(x - 2):
        b = a + b
        a = b - a
    return b


n = int(input())
print(fisich_n_fibb(n))
