"""
Only for quadratic equations.
仅针对一元二次方程。
"""
import math

print('For the equation ax^2+bx+c=0:')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

delta = b ** 2 - 4 * a * c
if delta < 0:
    print('The equation has no real roots.')
else:
    x1 = float((-b - math.sqrt(delta)) / (2 * a))
    x2 = float((-b + math.sqrt(delta)) / (2 * a))
    print(f'x1 = {str(x1)}')
    print(f'x2 = {str(x2)}')
