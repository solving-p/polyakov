def sum_ch(a):
    if a >= 10:
        return sum_ch(a // 10) + int(not (a & 1))
    return int(not (a & 1))


# n, m = map(int, input().split())
n = int(input())
print(sum_ch(n))
