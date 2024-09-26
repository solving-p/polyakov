def fisich_sum_del(x):
    if x == 1:
        return 0
    s = 1
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            s += i
            if i * i != x:
                s += x // i
    return s


f = True
a, b = map(int, input().split())
for i in range(a, b + 1):
    k = fisich_sum_del(i)
    if a <= k <= b and fisich_sum_del(k) == i and k != i and i < k:
        f = False
        print(f"({i},{k})", end=" ")
if f:
    print(0)
