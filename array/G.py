x, d, n = map(int, input().split())
print(*[x + d * (n - i - 1) for i in range(n)])
