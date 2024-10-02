n = int(input())
a = list(map(int, input().split()))
c = 0
k = 0
for i in a:
    if i < c or k == 0:
        k = 1
        c = i
for i in range(n):
    if a[i] == c:
        print(i + 1, end=" ")
print()
