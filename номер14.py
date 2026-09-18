# l = set()
# for x in "0123456789ABCDEFGHIJKLMNOPQRSTUV":
#   for y in "0123456789ABCDEF":
#     a = "52" + x + "H12"
#     b = "22" + x + "8"
#     c = "1" + y
#     if (int(a, 32) + int(b, 32)) % int(c, 16) == 0:
#       l.add(int(x, 32) + int(y, 16))
# print(len(l))


# summ = set()
#
# H = 17
# for x in range(32):
#     for y in range(16):
#         A = 5*(32**5) + 2*(32**4) + x*(32**3) + H*(32**2) + 1*32 + 2
#         B = 2*(32**3) + 2*(32**2) + x*32 + 8
#         S = A + B
#         delitel = 16 + y
#         if S % delitel == 0:
#             summ.add(x + y)
#
# print(len(summ))


# a = 2 * 2187**2020 + 729**2021 - 2 * 243**2022 + 81**2023 - 2 * 27**2024 - 6561
# k = 0
# while a > 0:
#     if a % 27 > 9.txt:
#         k += 1
#     a //= 27
# print(k)

                    # from string import *
                    #
                    # for x in printable[:29]:
                    #     a = int(f"923{x}874", 29) + int(f"524{x}6152", 29)
                    #     if a % 28 == 0:
                    #         print(x, a // 28)

# N = 23
# W = 32
# Y = 34
# A = 10
# R = 27
#
# pr = 1
# for x in range(190):
#   for y in range(190):
#     n = (N * 190**2 + x * 190 + W) + (Y * 190**3 + y * 190**2 + A * 190 + R)
#     if n % 189 == 0:
#       if x * y > pr:
#         pr = x * y
#         print(n // 189)

# from string import *
#
# for x in printable[:15]:
#   n = int(f"9897{x}21", 15) + int(f"12{x}023", 15)
#   if n % 14 == 0:
#     print(x, n // 14)

# n = 15 * 2401**1500 - 10 * 343**1200 + 40 * 49**1000 - 35 * 7**850 - 4805
# count = 0
# while n > 0:
#   if n % 49 > 9.txt:
#     count += 1
#   n //= 49
# print(count)

# for x in range(1, 2042):
#     n = 25**61 + 5**178 - x
#     count = 0
#     while n > 0:
#         if n % 5 == 0:
#             count += 1
#         n //= 5
#     if count == 60:
#         print(x)

for x in range(1_000_000, 1, -1):
    n = 25**340 + 25**79 - 5**60 + x
    count_0 = 0
    while n > 0:
        if n % 25 == 0:
            count_0 += 1
        n //= 25
    if count_0 == 287:
        print(x)
        break
