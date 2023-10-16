a = input().split()

b = list(a[0])
c = list(a[1])
d = len(b)
e = len(c)
f = [0 for i in range(d*e)]

for i in range(d-1, -1, -1):
    if (b[i] == '1'):
        for j in range(e-1, -1, -1):
            if c[j] == '1':
                f[(d*e)- 2 - (i+j)] += 1

vetor = []
h = len(f)
for i in range(h):
    if (f[i] == 1):
        if (i == h-1): 
            # print("1", end=())
            vetor.append('1')
        elif (i == h - 2):
            # print("x", end="")
            vetor.append('x')
        else:
            # print(f"x^{h-1-i}", end="")
            vetor.append(f"x^{h-1-i}")
o = len(vetor)

for i in range(o):
    if i == o-1:
        print(vetor[i])
    else:
        print(f'{vetor[i]} + ', end="")

