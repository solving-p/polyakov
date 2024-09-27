def prov(a):
    if a == 1:
        return True
    return prov(a // 2) and (a % 2 == 0)


n = int(input())
if prov(n):
    print("YES")
else:
    print("NO")
