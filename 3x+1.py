x = int(input('Enter a number: '))
print(int(x), end=' ')
count = 0
total = [1]
for i in range(1, 1000):
    while x != 1:
        if x % 2 == 1:
            x = 3 * x + 1
            count += 1
            total.append(x)
            print(int(x), end=' ')
        else:
            x = x / 2
            count += 1
            total.append(x)
            print(int(x), end=' ')
print(f'\nTimes: {count}')
print(f'Maximum: {max(total)}')
