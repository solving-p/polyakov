import sys


sys.setrecursionlimit(10 ** 6)


def fact(a, d):
    if d <= 1 or a == 1:
        return a
    a = fact(a, d - 1)
    while a % d == 0:
        print(d, end=" ")
        a //= d
    return a


n = int(input())
w = fact(n, int(n ** 0.5) + 1)
if w != 1 or n == 1:
    print(w)
else:
    print()
