x, n = map(int, input().split())
print(*[x + n - i - 1 for i in range(n)])
