a, b, c = map(int, input().split())

vet = []
vet.append(a)
vet.append(b)
vet.append(c)

vet.sort()

if 1 not in vet:
    print(1)
    
if 2 not in vet:
    print(2)

if 3 not in vet:
    print(3)

