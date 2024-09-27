def perevod_8_to_2(num, ost, pol):
    if num >= 3:
        c = 0
        if num % 3 + ost == 2 or num % 3 == 2:
            c = 1
        perevod_8_to_2(num // 3, c, pol)
        if num % 3 + ost == 2:
            if pol:
                print("1", end="")
            else:
                print("#", end="")
        elif num % 3 + ost == 3:
            print("0", end="")
        else:
            if pol and num % 3 + ost == 1:
                print("#", end="")
            else:
                print(num % 3 + ost, end="")
    else:
        if num % 3 + ost == 2:
            if pol:
                print("#1", end="")
            else:
                print("1#", end="")
        elif num % 3 + ost == 3:
            if pol:
                print("#0", end="")
            else:
                print("10", end="")
        else:
            if pol and num % 3 + ost == 1:
                print("#", end="")
            else:
                print(num % 3 + ost, end="")


n = int(input())
perevod_8_to_2(abs(n), 0, n < 0)
print()
