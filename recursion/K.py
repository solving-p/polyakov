def perevod_2_to_16(num):
    c = (num % 10) + (num // 10 % 10) * 2 + (num // 100 % 10) * 4 + (num // 1000 % 10) * 8
    if num >= 10000:
        perevod_2_to_16(num // 10000)
    if c < 10:
        print(c, end="")
    else:
        print(chr(c + ord("A") - 10), end="")


n = int(input())
if n < 0:
    print("-", end="")
perevod_2_to_16(abs(n))
print()
