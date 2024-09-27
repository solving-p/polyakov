def bin_n(a):
    if a >= 16:
        bin_n(a // 16)
    if a % 16 < 10:
        print(a % 16, end="")
    else:
        print(chr(ord("A") + a % 16 - 10), end="")


n = int(input())
if n < 0:
    print("-", end="")
bin_n(abs(n))
print()
