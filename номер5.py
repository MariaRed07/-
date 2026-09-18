
                              #Задание №5
# for n in range(1, 100):
#    s = bin(n)[2:] #перевод в двоичную систему
#    if s.count("1") % 2 == 0:
#        s += "00"
#    else:
#        s += "10"
#    r = int(s, 2) #перевод в десятичную систему)
#    if r > 43:
#        print(r)
#        break
#Складываются первая и вторая, а также вторая и третья цифры исходного числаю
#Полученные два числа записываются друг за другом в порядке убывания
# for i in range(100, 1000):
#    s = str(i)
#    k1 = int(s[0]) + int(s[1])
#    k2 = int(s[1]) + int(s[2])
#    first = str(max(k1, k2))
#    second = str(min(k1, k2))
#    s1 = first + second
#    if s1 == "1412":
#        print(i)
#        break

#Строится двоичная запись числа N.
#Все разряды полученного числа инвертируются.
#К полученному результату справа дописывается бит четности.
# a = []
# for n in range(1, 1000):
#  s = bin(n)[2:]
#  trans = str.maketrans({"1" : "0", "0" : "1"})
#  s = s.translate(trans)
#  s += str(s.count("1") % 2)
#  r = int(s, 2)
#  if r < 170:
#    a.append(r)
# print(max(a))
#
# #Строится двоичная запись числа N.
# #Из записи удаляются все нули.
# s = bin(n)[2:].replace("0", "").replace("1", "0")
#
# #Незначащие нули удаляются.
# s = s.lstrip("0")
# a = "".join(str(x) for x in a).lstrip("0")
# s = s.sort()


# !!! return s if s else "0"

for a in range(2):
    for b in range(2):
        if (a and (not b)) == 1:
            print(a, b)