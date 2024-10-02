n = int(input())
a = list(map(int, input().split()))
d, s = 0, 0
c, k = 0, 0
for i in range(n):
    if a[i] == c:
        k += 1
    if a[i] != c:
        c = a[i]
        k = 1
    if k > s:
        d = c
        s = k
print(d, s)
