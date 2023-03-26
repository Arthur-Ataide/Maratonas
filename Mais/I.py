N = int(input())
cont = 1
Vet = input().split()
aux = []
for i in Vet:
    aux.append(int(i))
aux.sort()
for c in range(1,N):
    if aux[c-1] != aux[c]:
        cont +=1
print(cont)