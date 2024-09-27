def max_v():
    c = int(input())
    if c == 0:
        return 0
    else:
        d = max_v()
        if c > d or d == 0:
            return c
        return d


print(max_v())
