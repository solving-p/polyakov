def bin_n(a, b):
    if a >= b:
        bin_n(a // b, b)
    if a % b < 10:
        print(a % b, end="")
    else:
        print(chr(ord("A") + a % b - 10), end="")


n, m = map(int, input().split())
if n < 0:
    print("-", end="")
bin_n(abs(n), m)
print()
