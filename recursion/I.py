def sum_ch(a):
    if a >= 2:
        return sum_ch(a // 10) * 2 + a % 10
    return a


# n, m = map(int, input().split())
n = int(input())
if n < 0:
    print("-", end="")
print(sum_ch(abs(n)))
