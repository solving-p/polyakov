def fisich_sov_number(x):
    s = 0
    if x > 1:
        s = 1
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            s += i
            if i * i != x:
                s += x // i
    return s == x


n = int(input())
if fisich_sov_number(n):
    print("YES")
else:
    print("NO")
