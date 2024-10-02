n = int(input())
a = list(map(int, input().split()))
x = int(input())
c = True
for i in range(n):
    if x == a[i]:
        c = False
        print(i + 1, end=" ")
if c:
    print(-1)
