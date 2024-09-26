def ya_funkciya(a):
    if a == 0:
        return 1
    k = 0
    while a:
        k += 1
        a //= 10
    return k


n = int(input())
print(ya_funkciya(n))
