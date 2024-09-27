def bin_n(a):
    if a < 8:
        print(a, end="")
        return
    bin_n(a // 8)
    print(a % 8, end="")


n = int(input())
if n < 0:
    print("-", end="")
bin_n(abs(n))
print()
