x, d, n = map(int, input().split())
print(*[x + i * d for i in range(n)])
