import math

f = open('answer.txt','w')
print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

discr = b ** 2 - 4 * a * c


if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    f.write(str(x1))
    f.write(str(x2))
elif discr == 0:
    x = -b / (2 * a)
    f.write(str(x))
else:
    f.write('0')

