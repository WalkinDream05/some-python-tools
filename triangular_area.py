"""
This program will calculate the triangular area(with Heron's formula)
计算三角形面积（利用海伦公式）
"""
import math

a = float(input('a='))
b = float(input('b='))
c = float(input('c='))

if a or b or c <= 0:
    print('The length should be positive!')
else:
    s = (a+b+c)/2
    A = float(math.sqrt(s*(s-a)*(s-b)*(s-c)))
    print('The area of the triangular is ' + str(A))
