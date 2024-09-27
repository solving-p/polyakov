def perevod_8_to_2(num):
    c = 0
    if num % 10 == 0:
        c = 0
    elif num % 10 == 1:
        c = 1
    elif num % 10 == 2:
        c = 10
    elif num % 10 == 3:
        c = 11
    elif num % 10 == 4:
        c = 100
    elif num % 10 == 5:
        c = 101
    elif num % 10 == 6:
        c = 110
    else:
        c = 111
    #
    if num >= 10:
        return perevod_8_to_2(num // 10) * 1000 + c
    return c


n = int(input())
if n < 0:
    print("-", end="")
print(perevod_8_to_2(abs(n)))
