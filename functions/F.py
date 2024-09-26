def fisich_rev(a):
    k = 0
    x = a
    while x:
        k += 1
        x //= 10
    k -= 1
    s = 0
    while k != -1:
        s += (10 ** k) * (a % 10)
        a //= 10
        k -= 1
    return s


n = int(input())
print(fisich_rev(n))
