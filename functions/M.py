def isprime(x):
    if x == 1:
        return 0
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


a, b = map(int, input().split())
r = True
for n in range(a, b + 1):
    f = True
    x = n
    while x:
        f &= isprime(x)
        x //= 10
    if f:
        r = False
        print(n, end=" ")
if r:
    print(0)
else:
    print()
