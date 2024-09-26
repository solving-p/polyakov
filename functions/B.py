def ya_funkciya(a, b, c, d, e):
    mmin = a
    mmax = a
    if b < mmin:
        mmin = b
    if c < mmin:
        mmin = c
    if d < mmin:
        mmin = d
    if e < mmin:
        mmin = e
    #
    if b > mmax:
        mmax = b
    if c > mmax:
        mmax = c
    if d > mmax:
        mmax = d
    if e > mmax:
        mmax = e
    return mmin, mmax, (a + b + c + d + e - mmin - mmax) / 3


x, y, z, n, m = map(int, input().split())
s, w, f = ya_funkciya(x, y, z, n, m)
print(s, w)
print(f"{f:.2f}")
