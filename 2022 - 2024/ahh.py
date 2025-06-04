N,M = map(int,input().split())

while N >= 2  and M >= 2:
    vet = []
    aux = []
    teste = []
    
    contagem_numeros = {}

    for i in range(N):
        vetor = map(int, input().split())  
        for num in vetor:
            contagem_numeros[num] = contagem_numeros.get(num, 0) + 1

    aux = sorted(contagem_numeros.items(), key=lambda x: (x[1], x[0]))

    segundo = aux[-2][1]
    vetor = [str(num) for num, contagem in aux if contagem == vetor]

    print(" ".join(vetor))

    
    