import sys


sys.setrecursionlimit(10 ** 6)


def prov(a, d):
    if d <= 1:
        return True
    if a % d == 0:
        return False
    return prov(a, d - 1)


n = int(input())
if prov(n, int(n ** 0.5)) and n != 1:
    print("YES")
else:
    print("NO")
