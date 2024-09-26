def isprime(x):
    if x == 1:
        return 0
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


n = int(input())
f = True
while n:
    f &= isprime(n)
    n //= 10
if f:
    print("YES")
else:
    print("NO")
