def bin_n(a):
    if a < 2:
        print(a, end="")
        return
    bin_n(a // 2)
    print(a % 2, end="")


n = int(input())
if n < 0:
    print("-", end="")
bin_n(abs(n))
print()
