
                    #Задание №23
#Прибавить 1
#Прибавить 2
#Умножить на 2
# def f(x, y):
#    if x > y:
#        return 0
#    if x == y:
#        return 1
#    else:
#        return f(x + 1, y) + f(x + 2, y) + f(x * 2, y)
# print(f(3, 10) * f(10, 12))

#ограничение по кол-во команд (тут меньше 15 команд)
# def f(x, y, k):
#     if x > y or x == 27 or k > 15:
#         return 0
#     if x == y:
#         return 1
#     return f(x+2, y, k+1) + f(x*3, y, k+1) + f(x**3, y, k+1)
#
# print(f(3, 125, 0))


# Сколько различных чисел может получиться при начальном числе 2 в ходе работы исполнителя,
# если известно, что программа состоит из 5 команд?
# num = {2}
# for _ in range(5):
#   num = {x+4 for x in num} | {x*2 for x in num}
# print(len(num))



# Сколько существует непустых программ, для которых при исходном
# чётном положительном числе результатом работы является число 15?
# def f(x, y):
#   if x > y:
#     return 0
#   if x == y:
#     return 1
#   else:
#     return f(x+1, y) + f(x*2, y) + f(x*3, y)
#
# k = 0
# for x in range(2, 16, 2):
#   k += f(x, 15)
# print(k)


# def f(x, y):
#     if x > y or x == 81:
#         return 0
#     if x == y:
#         return 1
#     else:
#         return f(x + int(str(x)[0]), y) + f(x + 3, y) + f(2 * x - 1, y)
#
# print(f(42, 73) * f(73, 89))


# from turtle import *
# tracer(0)
# screensize(3000, 3000)
# left(90)
# k = 20
#
# pd()
# right(90)
# for _ in range(2025):
#     forward(10*k)
#     right(90)
#     forward(5*k)
#     right(90)
# pu()
# forward(7*k)
# right(120)
# pd()
# for _ in range(6):
#     forward(5*k)
#     right(120)
# pu()
#
# for x in range(-100, 100):
#     for y in range(-100, 100):
#         goto(x*k, y*k)
#         dot(5)
# done()


# from math import *
# for n in range(100, 1_000):
#     s = []
#     for d in str(n):
#         s.append(int(d))
#     pr = prod(s)
#     sm = sum(s)
#     if pr < sm:
#         r = str(sm) + str(pr)
#     else:
#         r = str(pr) + str(sm)
#     r = int(r)
#     if r == 24019:
#         print(n)


# for A in range(256):
#     ip = (32 << 24) + (0 << 16) + (A << 8) + 5
#     mask = (255 << 24) + (255 << 16) + (240 << 8)
#     net = ip & mask
#     n = f'{mask:b}'.count('0')
#     ips = [net + x for x in range(2**n)]
#     if all(f'{(ip >> 16) & (2**16 - 1):b}'.count('1') <= f'{ip & (2**16 - 1):b}'.count('1') for ip in ips):
#         print(A)
#         break

print(bin(199)[2:].zfill(8), bin(59)[2:].zfill(8), bin(129)[2:].zfill(8), bin(3)[2:].zfill(8))
11000111 00111011 10000001 00000011
11111111 11111111          00000000
