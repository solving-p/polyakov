def sum_ch(a):
    if a >= 10:
        return sum_ch(a // 10) + (a % 10)
    return a


# n, m = map(int, input().split())
n = int(input())
print(sum_ch(n))
