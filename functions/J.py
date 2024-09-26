def fisich_sum_cifr(x):
    s = 0
    while x:
        s += x % 10
        x //= 10
    return s


f = True
a, b = map(int, input().split())
for i in range(a, b + 1):
    k = fisich_sum_cifr(i)
    for j in range(2, 10):
        if fisich_sum_cifr(i * j) != k:
            break
    else:
        f = False
        print(i, end=" ")
if f:
    print(0)
else:
    print()
