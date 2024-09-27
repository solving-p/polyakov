def perevod_8_to_2(num, osn):
    if num >= 10:
        return perevod_8_to_2(num // 10, osn) * osn + num % 10
    return num % 10


# n = int(input())
b, a = map(int, input().split())
if a < 0:
    print("-", end="")
print(perevod_8_to_2(abs(a), b))
