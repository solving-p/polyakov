def perevod_2_to_8(num):
    c = (num % 10) + (num // 10 % 10) * 2 + (num // 100 % 10) * 4
    if num >= 1000:
        return perevod_2_to_8(num // 1000) * 10 + c
    return c


n = int(input())
if n < 0:
    print("-", end="")
print(perevod_2_to_8(abs(n)))
