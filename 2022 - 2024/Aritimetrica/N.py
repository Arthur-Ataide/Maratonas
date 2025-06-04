a = list(input())
bi = 0
e = len(a)

for c in range(e-1, -1, -1):
    d = int(a[c])
    if a[c] == '1':
        bi += 2**(e - c-1)

print(bi)
