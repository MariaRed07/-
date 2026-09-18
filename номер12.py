# flag = False
# for i in range(500): #i - количество 0 и 1
#     for j in range(500): #j - количество 2 в начальной строке
#         s = i  * "0" + i * "1" + j * "2"
#         if len(s) != 1000: #условие задачи, длина больше 1000
#             continue
#         s = list(s) #преобразовываем строку в список
#         sum1 = sum(map(int, s))
#         for k in range(len(s)):
#             if s[k] == "0":
#                 s[k] == "1"
#             elif s[k] == "1":
#                 s[k] == "2"
#             elif s[k] == "2":
#                 s[k] == "0"
#         sum2 = sum(map(int, s))
#         if (sum1 - sum2) == 200:
#             print(j)
#             flag = True
#             break
#     if flag:
#         break

# flag = False
# for i in range(1201):  # кол-во нулей
#     for j in range(1200 - i):  # кол-во 1
#         p = 1200 - i - j  # кол-во двоек
#         if p < 0:
#             continue
#         if (i + p) == j:  # кол-во четных равно кол-во нечетных
#             if (j + 2 * p) == 800:  # сумма цифр по условию равно 800
#                 print(i)
#                 flag = True
#                 break
#     if flag:
#         break

