# 1 тип
# import sys
# sys.setrecursionlimit(3000) #это может не требоваться, нужно если функция большая, подстравиваемся под значение функции
# def f(n):
#     if n < 3:
#         return 1
#     if n % 2 != 0:
#         return f(n - 1) + n
#     if n % 2 == 0:
#         return f(n - 3) + 2 * n
# print(f(2048) - f(2041))

# 2 тип
# from functools import lru_cache
#
# @lru_cache(None) #декаратор
# def f(n):
#     if n <= 1:
#         return 42
#     if n > 1 and n % 2 == 0:
#         return f(n - 2) + f(n - 3) + n
#     else:
#         return f(n - 1) + f(n - 3) - n
#
#  #желательно двойной разрыв
# print(f(99))


# 3 тип
# def f(n):
#     if n <= 2 or n == 8:
#         return 0
#     elif n == 3:
#         return 1
#     elif n > 3 and n != 8:
#         return f(n -3) + f(n -1)
#
#
# for n in range(1000):
#     if f(n) == 25:
#         print(n)

# from functools import lru_cache
#
# @lru_cache(None)
# def f(n):
#   if n >= 10000:
#     return 1
#   if n < 10000 and n % 2 == 0:
#     return f(n + 3) + 7
#   else:
#     return f(n + 1) - 3
#
# print(f(50)- f(57))