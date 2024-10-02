n = int(input())
a = list(map(int, input().split()))
m1, m2, m3 = 0, 0, 0
for i in range(n):
    if a[i] < m1 or i == 0:
        m1, m2, m3 = a[i], m1, m2
    elif a[i] < m2 or i == 1:
        m2, m3 = a[i], m2
    elif a[i] < m3 or i == 2:
        m3 = a[i]
print(m1, m2, m3)
