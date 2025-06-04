a = input().split()

b = len(a)

for i in range(b):
    a[i] = int(a[i])

a.sort()

for i in range(b):
    if b-1 != i:
        print(a[i], end=(' '))
    else:
        print(a[i])

for i in range(b-1, -1, -1):
    if 0 != i:
        print(a[i], end=(' '))
    else:
        print(a[i])

