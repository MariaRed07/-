# from turtle import *
# tracer (0) #отключение пошаговой генерации
# left(90) #поворот в оси ординат
# #ничего если по оси абсцисс
# k = 20 #масштабирование, нужно чтобы поле с точками выглядело адекватно, можно и 10
# screensize(3000, 3000) #рамзер поля
#
# pd()
# right(90)
# begin_fill()
# for _ in range(3):
#     right(45)
#     forward(10 * k)
#     right(45)
# right(315)
# forward(10 * k)
# for _ in range(2):
#     right(90)
#     forward(10 * k)
# end_fill()
# pu()
#
# canvas = getcanvas() # только подсчет точек без точек на линии
# cnt = 0
# for x in range(-100, 100):
#     for y in range(-100, 100):
#         goto(x * k, y * k)
#         dot(5)
#         info = canvas.find_overlapping(x * k, y * k, x * k, y * k)
#         if len(info) == 1 and info[0] == 5:
#             cnt += 1
# print(cnt)
# done() #чтобы сразу все не обнулилось


from turtle import *
screensize(3000, 3000)
tracer(0)
k = 20
left(90)

pd()
right(90)
begin_fill()
for _ in range(3):
    right(45)
    forward(10 * k)
    right(45)
right(315)
forward(10 * k)
for _ in range(2):
    right(90)
    forward(10 * k)
end_fill()
pu()

canvas = getcanvas()
cnt = 0
for x in range(-100, 100):
    for y in range(-100, 100):
        info = canvas.find_overlapping(x * k, y * k, x * k, y * k)
        if len(info) > 0: #автоподсчет с линиями !!но если точки начала координат в фигуре
            cnt += 1
        if len(info) > 0:
            print(x, y, info)
for x in range(-30 , 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        if x == 0 or y == 0:
            dot(5, "red")
        else:
            dot(5, "blue")
print(cnt)
done()