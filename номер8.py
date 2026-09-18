                                  #Задание №8
#5-ти буквунные слова, есть только буквы "abcx" причем х может появится на последнем месте или не появиться вовсе.
#Сколько различных кодовых слов можно использовать?
# from itertools import product
# k = 0
# words = product("abcx", repeat=5)
# for w in words:
#     word = "".join(w)
#     if (word[-1] == "x" and word.count("x") == 1) or word.count("x") == 0:
#         k += 1
# print(k)

# k = 0
# letters = "abcx"
# for i1 in letters:
#     for i2 in letters:
#         for i3 in letters:
#             for i4 in letters:
#                 for i5 in letters:
#                     word = i1 + i2 + i3 + i4 + i5
#                     if (word[-1] == "x" and word.count("x") == 1) or word.count("x") == 0:
#                         k+= 1
# print(k)

 

from itertools import permutations
slovo = "КОБУРА"
vowels = "ОУА"
count = 0
for word in permutations(slovo):
    flag = True
    for i in range(5):
        if (word[i] in vowels) == (word[i + 1] in vowels):
            flag = False
            break
    if flag:
        count += 1
print(count)