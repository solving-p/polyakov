def sum_ch(a):
    if a >= 10:
        c = sum_ch(a // 10)
        if a % 10 > c:
            return a % 10
        return c
    return a


# n, m = map(int, input().split())
n = int(input())
print(sum_ch(n))
