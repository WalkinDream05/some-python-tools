"""
If it is even, calculate x / 2
If it is odd, calculate 3 * x + 1
偶数：计算x / 2
奇数：计算3 * x + 1
"""

while True:
    x = input("Enter a number, and I will calculate for you(Enter 'q' to quit): ")
    if x != 'q':
        x = int(x)
        print(int(x), end=' ')
        COUNT = 0
        total = [1]
        for i in range(1, 1000):
            while x != 1:
                if x % 2 == 1:
                    x = 3 * x + 1
                    COUNT += 1
                    total.append(int(x))
                    print(int(x), end=' ')
                else:
                    x = x / 2
                    COUNT += 1
                    total.append(int(x))
                    print(int(x), end=' ')
        print(f'\nTimes: {COUNT}')
        print(f'Maximum: {max(total)}')
    else:
        break
