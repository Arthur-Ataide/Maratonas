N, K = map(int, input().split())

vet = [[0 for _ in range(4)] for _ in range(N)]

menor = 0

for i in range(N):
    vet[i][0], vet[i][1] = map(int, input().split())
    vet[i][2] = 1
    vet[i][3] = 0
    if (i == 0):
        menor = vet[i][0]
        
    else:
        if (vet[i][0] < menor):
            menor = vet[i][0]

cont = 0
tempo = 0

while(cont < K):
    
    tempo += menor
    
    for i in range(N):
        if(i == 0):
            if (vet[i][2]):
                if(vet[i][0] <= tempo - vet[i][3]):
                    cont += 1
                    vet[i][3] += vet[i][0]
                    vet[i][2] = 0
                    menor = vet[i][3] + vet[i][1] - tempo
                    
                else: 
                    menor = vet[i][3] + vet[i][0] - tempo
                    
                        
            else:
                if(vet[i][1] <= tempo - vet[i][3]):
                    cont += 1
                    vet[i][3] += vet[i][1]
                menor = vet[i][3] + vet[i][1] - tempo
                    
        else:
            if (vet[i][2]):
                if(vet[i][0] <= tempo - vet[i][3]):
                    cont += 1
                    vet[i][3] += vet[i][0]
                    vet[i][2] = 0
                    if (menor > vet[i][3] + vet[i][1] - tempo):
                        menor = vet[i][3] + vet[i][1] - tempo
                    
                else:
                    if menor > vet[i][3] + vet[i][0] - tempo:
                        menor = vet[i][3] + vet[i][0] - tempo
                    
                        
            else:
                if(vet[i][1] <= tempo - vet[i][3]):
                    cont += 1
                    vet[i][3] += vet[i][1]
                
                if (menor > vet[i][3] + vet[i][1] - tempo):
                    menor = vet[i][3] + vet[i][1] - tempo
            
        
print(tempo)

# 2 10              
# 5 3
# 10 4