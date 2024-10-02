n = int(input())
a = list(map(int, input().split()))
x = int(input())
c = 0
for i in a:
    if i == x:
        c += 1
print(c)
