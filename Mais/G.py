v = input().split()
vet = []
for c in range(len(v)):
    vet.append(int(v[c]))
cont = 1
vet.sort()
print(vet[0], end = " ")
for c in range(1,len(vet)):
    if vet[c-1] == vet[c]:
        cont +=1
    else:
        print(cont)
        cont = 1
        print(vet[c], end = " ")
print(cont)