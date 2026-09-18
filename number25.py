# from fnmatch import *
# for x in range(1, 10**10, 1917): #шаг число на которой должно делиться
#     if fnmatch(str(x), "4*4736*1"): #число = маска данная в условие
#         print(x, x//1917)

# def d(x):
#     d = set()
#     for i in range(2, int(x**0.5) + 1):
#         if x % i == 0:
#             d |= {i, x// i} #apdate добвление в массив == append
#     return sorted(d)
#
# k = 0
# for x in range(800_000, 900_000):
#     f = d(x)
#     M = f[0] + f[-1] if f else 0
#     if M % 10 == 4:
#         print(x, M)
# def n(x):
#     for i in range(2, int(x**0.5) + 1):
#         if x % i == 0:
#             return 0
#     return 1
#
# def f(x):
#     d = set()
#     for i in range(2, int(x**0.5) + 1):
#         if x % i == 0:
#             d |= {i, x//i}
#     return sorted(d)
#
# k = 0
# for x in range(13_200_001, 14_000_000):
#     d = []
#     for i in f(x):
#         if n(i):
#             d.append(i)
#     M = d[0] + d[-1] if len(d) > 0 else 0
#     if M > 30_000 and M % 100 == 55:
#         print(x, M)
#         k += 1
#         if k == 7:
#             break




# from fnmatch import *
# for x in range (0, 10**10, 7993):
#     if fnmatch(str(x), "4*4736*1"):
#         print(x, x//7993)

# from fnmatch import *
# for x in range(0, 10**10, 18579):
#     if fnmatch(str(x), "54?1?3*7"):
#         print(x, x//18579)

# from fnmatch import *
# for x in range(0, 10**10, 2025):
#      if fnmatch(str(x), "21?5846*?"):
#          if x % 2025 == 0:
#             print(x, x//2025)

# from fnmatch import *
# for x in range(0, 10**10, 98591):
#     if fnmatch(str(x), "5?2*3?3?"):
#         print(x, x//98591)

# from fnmatch import *
# for x in range(0, 10**12, 98591):
#     if fnmatch(str(x), "5?2*3?3?"):
#         print(x, x//98591)

# def prost(x):
#     for i in range(2, int(x**0.5) + 1):
#         if x % i == 0:
#             return 0
#     return 1
#
# def div(x):
#     div = set()
#     for i in range(2, int(x**0.5) + 1):
#         if x % i == 0:
#             div |= {i, x//i}
#     return sorted(div)
#
# k = 0
# for x in range(7_800_000, 8_800_000):
#     delet = []
#     for i in div(x):
#         if prost(i):
#             delet.append(i)
#     M = delet[0] + delet[-1] if len(delet) > 0 else 0
#     if M % 100 == 63 and M % len(delet) == 0:
#         print(x, M)
#         k += 1
#         if k == 5:
#             break


