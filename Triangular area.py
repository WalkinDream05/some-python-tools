import math

a = float(input('a='))
b = float(input('b='))
c = float(input('c='))

if a or b or c <= 0:
    print('边应为正数!')
else:
    s = (a+b+c)/2
    A = float(math.sqrt(s*(s-a)*(s-b)*(s-c)))
    print('The area of the triangular is ' + str(A))
