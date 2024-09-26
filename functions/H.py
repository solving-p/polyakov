def fisich_sum_del(x):
    s = 1
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            s += i
            if i * i != x:
                s += x // i
    return s


a, b = map(int, input().split())
if a == fisich_sum_del(b) and b == fisich_sum_del(a):
    print("YES")
else:
    print("NO")
