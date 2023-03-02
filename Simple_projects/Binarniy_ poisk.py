from random import randint

n = int(input())
x = randint(1, n)
left, right, count = 1, n, 0
middle = (left + right) // 2
while middle != x:
    if middle > x:
        right = middle - 1
        middle = (left + right) // 2
        count += 1
    elif middle < x:
        left = middle + 1
        middle = (left + right) // 2
        count += 1
else:
    if count == 0:
        print(1)
    else:
        print(count)