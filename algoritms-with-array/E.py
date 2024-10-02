n = int(input())
a = list(map(int, input().split()))
c, k = -1, -1
for i in range(n):
    if a[i] >= 0 and a[i] % 2 == 0 and (a[i] > c or c == -1):
        c = a[i]
    if a[i] >= 0 and a[i] % 2 == 0 and (a[i] < k or k == -1):
        k = a[i]
print(k, c)
