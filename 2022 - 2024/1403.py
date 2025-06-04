N,M = map(int,input().split())

while N >= 2  and M >= 2:
    vet = []
    aux = []
    teste = []
    
    contagem_numeros = {}  

    for i in range(N):
        vetor = input().split()
        for j in range(M):
            num = int(vetor[j])  
            if num in contagem_numeros:
                contagem_numeros[num] += 1
            else:
                contagem_numeros[num] = 1

    aux = [[num, contagem] for num, contagem in contagem_numeros.items()]

    
    aux.sort(key=lambda x: (x[1], x[0]))
    
    num = aux[-2][1]
    
    for i in range(len(aux)-1):
        if aux[i][1] == num:
                print(aux[i][0], end = " ")
    print()    
    N,M = map(int,input().split())

    
    