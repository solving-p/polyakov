n = int(input())
a = list(map(int, input().split()))
c, k = 0, 0
for i in range(n):
    if a[i] == c:
        k += 1
    if a[i] > c or k == 0:
        c = a[i]
        k = 1
print(c, k)
