#                     #Задание № 15
# !!!for x in [k*0.25 for k in range(-10_000, 10_000)]

#Если дан некий отрезок В =[50, 70]
# b = list(range(50, 71))
# for a in range(100000, 1, -1):
#     flag = True
#     for x in range(1, 10000):
#         if ((x % a == 0) or (x % 23 == 0) <= (not (x in b))) == False:
#             flag = False
#             break
#     if flag:
#         print (a)
#         break


# for A in range(1, 100000):
#     ok = True
#     for x in range(1, 100000):
#         y = 78125 - 4 * x
#         if y <= 0:
#             continue
#
#         if (A<= x) or (A <= y):
#             ok = False
#             break
#     if ok:
#         print(A)
#         break


# def f(x):
#     A = 7 <= x <= 26
#     B = 77 % x == 0 and x != 1 and x != 77
#     C = y % x == 0 and x != 1 and x != y
#     return C <= (A and (not B))
#
# for y in range(1, 10_000):
#     if any(y % x == 0 for x in range(2, y)):
#         if all(f(x) for  x in range(1, 100_000)):
#             print(y)
#             break

#Найти количество R, при котором тождество истинно при любом А
# k = 0
# for r in range(1, 1000):
#     flag = True
#     for x in range(1, 1000):
#         for a in range(1, 1000):
#             if ( (((x&37==0) or (x&59==0)) <= (x&a==0)) or (x&r==0) ) == False:
#                 flag = False
#                 break
#         if not flag:
#             break
#     if flag:
#         k += 1
# print(k)

# def f(x, y):
#     return (x*y<a) or (x<7*y) or (343<x)
# for a in range(1000):
#     if all(f(x, y) for x in range(1000) for y in range(1000)):
#         print(a)
#         break

# def check(A):
#     for x in range(30):
#         for y in range(x):
#             if (3*x + y) > A:
#                 return False
#     return True
#
# for A in range(200):
#     if check(A):
#         print(A)
#         break

# def check(A):
#     # x может быть больше 24, но тогда условие (x > 24) истинно, так что проверять не нужно
#     # Достаточно проверить x от 0 до 24, y от 0 до некоторого разумного предела
#     for x in range(0, 25):  # x ≤ 24
#         for y in range(0, 50):  # достаточный предел из условий
#             if not ((3*y - x > 12) or (2*x + 6*y >= 72) or (x > 24) or (x*y < A)):
#                 return False
#     return True
#
# for A in range(200):
#     if check(A):
#         print(A)
#         break


# P = list(range(25, 65))
# Q = list(range(40, 116))
# A = []
#
# for x in range(25, 116):
#   if ((x in P) <= (((x in Q) and not (x in A)) <= (not(x in P)))) == 0:
#     A.append(x)
# print(len(A) - 1)

# P = list(range(17, 59))
# Q = list(range(29, 81))
# A = []
#
# for x in range(17, 81):
#     if ((x in P) <= (((x in Q) and not(x in A)) <= (not(x in P)))) == 0:
#         A.append(x)
# print(len(A) - 1)


# B = list(range(36, 76))
# C = list(range(60, 111))
# A = []
#
# for x in range(36, 111):
#     if (not(x in A) <= ((x in B) == (x in C))) == 0:
#         A.append(x)
# print(len(A) - 1)
#
# P = list(range(15, 41))
# Q = list(range(21, 64))
# A = []
#
# for x in range(15, 64):
#     if ((x in P) <= (((x in Q) and not (x in A)) <= (not (x in P)))) == 0:
#         A.append(x)
# print(len(A) - 1)


# P = list(range(15, 40))
# Q = list(range(21, 64))
# A = []
#
# for x in range(15, 64):
#     if ((x in P) <= (((x in Q) and not (x in A)) <= (not (x in P)))) == 0:
#         A.append(x)
# print(len(A) - 1)

# B = list(range(24, 91))
# C = list(range(47, 116))
# A = []
#
# for x in range(24, 116):
#     if ((x in C) <= ((not(x in A) and (x in B)) <= (not(x in C)))) == 0:
#         A.append(x)
# print(len(A) - 1)

# D = list(range(7, 69))
# C = list(range(29, 101))
# A = []
#
# for x in range(7, 101):
#     if ((x in D) <= ((not(x in C) and not(x in A)) <= (not(x in D)))) == 0:
#         A.append(x)
# print(len(A))


# def f(x):
#     return (x % 128 == 0) <= (x % A != 0) <= (x % 80 != 0)
#
# for A in range(1_000_000_000, 1, -1):
#     if all(f(x) == 1 for x in range(1, 1_000)):
#         print(A)
#         break

# def f(x):
#     return ((x % A != 0) <= ((x % 28 == 0) <= (x % 49 != 0)))
#
# for A in range(1_000, 1, -1):
#     if all(f(x) == 1 for x in range(1, 1_000_000)):
#         print(A)
#         break

# def f(x):
#     return ((x % A == 0) or ((x in B) <= (x % 22 != 0)))
#
# B = list(range(70, 91))
# for A in range(1_000, 1, -1):
#     if all(f(x) == 1 for x in range(1, 1_000_000)):
#         print(A)
#         break

# def f(x):
#     return ((x % A == 0) or ((x in B) <= (x % 22 != 0)))
#
# B = list(range(60, 81))
# for A in range(1_000, 1, -1):
#     if all(f(x) == 1 for x in range(1_000_000, 1)):
#         print(A)
#         break

# def f(x):
#     return ((x & A == 0) or (x & 37 != 0) or (x & 12 != 0))
#
# for A in range(1_000, 1, -1):
#     if all(f(x) == 1 for x in range(1, 1_000_000)):
#         print(A)
#         break

# def f(x):
#     return ((x & A != 0) <= ((x & 168 == 0) <= (x & 69 != 0)))
#
# for A in range(1_000, 1, -1):
#     if all(f(x) == 1 for x in range(1, 1_000_000)):
#         print(A)
#         break


# def f(x):
#     return (((x & 52 != 0) and (x & 48 == 0)) <= (x & A != 0))
#
# for A in range(1, 1_000):
#     if all(f(x) == 1 for x in range(1, 1_000_000)):
#         print(A)
#         break

#
# def f(x):
#     return (x & 39 == 0 or (x & 11 == 0 <= (x % A != 0)))
#
# for A in range(1, 1_000_000_000):
#     if all(f(x) == 1 for x in range(1, 1_000)):
#         print(A)
#         break

# def f(x, y):
#     return ((x - 3*y < A) or (y > 400) or (x > 56))
#
# for A in range(1, 1_000):
#     if all(f(x, y) == 1 for x in range(1, 1_000) for y in range(1, 1_000)):
#         print(A)
#         break


# def f(x, y):
#     return ((5 < y) or (x > 32) or (x + 2*y < A))
#
# for A in range(1, 1_000):
#     if all(f(x, y) == 1 for x in range(1, 1_000) for y in range(1, 1_000)):
#         print(A)
#         break

# def f(x, y):
#     return ((x * y > A) or (x > y) or (11 > x))
#
# for A in range(1_000, 1, -1):
#     if all(f(x, y) for x in range(1, 1_000) for y in range(1, 1_000)):
#         print(A)
#         break


# def f(x, y):
#     return ((2*x + y != 110) or (x < y) or (A < x))
#
# for A in range(1_000, 1, -1):
#     if all(f(x, y) == 1 for x in range(1, 1_000) for y in range(1, 1_000)):
#         print(A)
#         break


# def f(x, y):
#     return ((x < A) and (y < 3*A) or (2*x + y > 128))
#
# for A in range(1, 1_000):
#     if all(f(x, y) == 1 for x in range(1, 1_000) for y in range(1, 1_000)):
#         print(A)
#         break


#

# def f(x):
#     return (x % 128 == 0) <= ((x % A != 0) <= (x % 80 != 0))
#
# for A in range(1_000, 1, -1):
#     if all(f(x) == 1 for x in range(1, 1_000_000)):
#         print(A)
#         break

# def f(x):
#     return ((x & 39 == 0) or ((x & 11 == 0) <= (x & A != 0)))
#
# for A in range(1, 1_000):
#     if all(f(x) == 1 for x in range(1, 1_000_000)):
#         print(A)
#         break


# def f(x):
#     return (x % A != 0) <= ((x % 14 == 0) <= (x % 4 != 0))
#
# for A in range(1_000, 1, -1):
#     if all(f(x) == 1 for x in range(1, 1_000_000)):
#         print(A)
#         break


# def f(x, y):
#     return (x*y > A) or (x > y) or (11 > x)
#
# for A in range(1_000, 1, -1):
#     if all(f(x, y) == 1 for x in range(1, 1_000) for y in range(1, 1_000)):
#         print(A)
#         break


# def f(x, y):
#     return (x**2 <= 136) or (y < (4*x + A - 70)) or (2*y > 51)
#
# for A in range(1, 1_000):
#     if all(f(x, y) == 1 for x in range(1, 1_000) for y in range(1, 1_000)):
#         print(A)
#         break


# def f(x):
#     return (x & 117 != 0) and (x & 91 == 0) <= (x & A != 0)
#
# for A in range(1, 1_000_000_0):
#     if all(f(x) == 1 for x in range(1, 1_000)):
#         print(A)
#         break