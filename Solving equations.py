import math

print('对于方程ax^2+bx+c=0')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

delta = b ** 2 - 4 * a * c
if delta < 0:
    print('方程无实数根')
else:
    x1 = float((-b - math.sqrt(delta)) / (2 * a))
    x2 = float((-b + math.sqrt(delta)) / (2 * a))
    print(f'x1 = {str(x1)}')
    print(f'x2 = {str(x2)}')
