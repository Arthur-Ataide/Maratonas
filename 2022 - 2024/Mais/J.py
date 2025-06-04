N = int(input())
v = input().split()
timeA = []
timeB = []
vet = []
a = []
b = []

for c in v:
    vet.append(int(c))
vet.sort(reverse=True)

for c in range(int(N/2)):
    timeA.append(vet[c*2])
    timeB.append(vet[c*2 + 1])
if N%2 == 1:
    timeB.append(vet[N-1])
for c in timeA:
    a.append(c)

for c in timeB:
    b.append(c)

for i in range(len(a)):
    if len(a)-1 != i:
        print(a[i], end=(' '))
    else:
        print(a[i])

for i in range(len(b)):
    if len(b)-1 != i:
        print(b[i], end=(' '))
    else:
        print(b[i])
