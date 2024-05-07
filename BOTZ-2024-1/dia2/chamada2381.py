N, K = map(int, input().split())

vet = []

for i in range(N):
    a = str(input())
    vet.append(a)
    
    
vet.sort()
print(vet[K-1])

# 5 1
# maria
# joao
# carlos
# vanessa
# jose