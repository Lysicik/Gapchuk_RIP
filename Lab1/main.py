

from math import sqrt
import math

print('Гапчук Людмила ИУ5-51Б')
print("ax^4+bx^2+c=0")

flag = True
while (flag):
    try:
        a = float(input("Введите a\n"))
        flag = False
    except ValueError:
        flag = True


flag = True
while (flag):
    try:
        b = float(input("Введите b\n"))
        flag = False
    except ValueError:
        flag = True


flag = True
while (flag):
    try:
        c = float(input("Введите c\n"))
        flag = False
    except ValueError:
        flag = True


if a == 0 and b == 0 and c == 0:
    print('x - любое число')

elif c != 0 and b == 0 and a == 0:
    print('Нет решений')

elif b != 0 and a == 0:
    x = -c / b
    if x < 0:
        print('Нет действительных корней')
    elif x == 0:
        print('x = 0')
    else:
        print('x1 = %.2f' % (sqrt(x)) + ' x2 = %.2f' % (-sqrt(x)))

else:
    d = b ** 2 - 4 * a * c

    if d < 0:
        print('т.к D < 0. Нет действительных корней.')

    else:
        t1, t2 = ((-b + sqrt(d)) / 2 * a), ((-b - sqrt(d)) / 2 * a)

        if t1 < 0 and t2 < 0:
            print('Нет действительных корней')

        elif t1 > 0:
            print('x1 = %.2f' % (-1 * sqrt(t1)))
            print('x2 = %.2f' % (sqrt(t1)))
        elif t1 == 0:
            print('x = 0')
        if t2 > 0 and t1 != t2:
            print('x1 = %.2f' % (-1 * sqrt(t2)))
            print('x2 = %.2f' % (sqrt(t2)))
        elif t2 == 0 and t1 != t2:
            print('x = 0')

