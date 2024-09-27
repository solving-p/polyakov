def max_v():
    c = int(input())
    if c == 0:
        return 0, 0
    else:
        d, k = max_v()
        if c > d or d == 0:
            return c, 1
        elif c == d:
            return d, k + 1
        return d, k


a, b = max_v()
print(b)
