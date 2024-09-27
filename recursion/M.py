def perevod_8_to_2(num):
    if num >= 10:
        return perevod_8_to_2(num // 10) * 8 + num % 10
    return num % 10


n = int(input())
if n < 0:
    print("-", end="")
print(perevod_8_to_2(abs(n)))
