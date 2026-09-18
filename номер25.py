def f(x):
    delit = []
    for d in range(1, int(x**0.5) + 1):
        if x % d == 0:
            delit.append(d)
            if d != x // d:
                delit.append(x // d)
    delit.sort()
    return delit
x = 700_001
count = 0
while count != 6:
    s = f(x)
    if len(s) == 4:
        a = s[2] - s[1]
        if a <= 15:
            count += 1
            print(x, a)
    x += 1