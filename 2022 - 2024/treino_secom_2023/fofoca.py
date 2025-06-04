n = int(input())

vet = input().split()


for i in range(n):
    vet[i] = int(vet[i])

i = 0

vet.sort(reverse=True)
print(vet)

cont = 0

if n == 1:
    print(0)
    exit()

if n == 2:
    print(vet[0] - vet[1])
    exit()

while True:
    
    if sum(vet) == 0 or sum(vet) == vet[0]:
        break
    
    sub = vet[1] - vet[2] + 1
    vet[0] -= sub
    vet[1] -= sub
    cont = sub
    vet.sort(reverse=True)
    print(vet)
    
    
    
print(cont)
