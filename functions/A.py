def ya_funkciya(a, b, c):
    if b < a:
        a = b
    if c < a:
        a = c
    return a


x, y, z = map(int, input().split())
print(ya_funkciya(x, y, z))
