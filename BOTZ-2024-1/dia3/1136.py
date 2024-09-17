N, B = map(int, input().split())

while(1):
    if (B == 0 and N == 0):
        exit()
    
    vet = input().split()
    
    cont = [0 for i in range(N+1)]

    if('0' not in vet or str(N) not in vet):
        print('N')

    
    else:
        cont[0] = 1
        cont[-1] = 1

        for i in range(B):
            for j in range(B- i):
                cont[abs(int(vet[i])-int(vet[j]))] = 1

        if (0 in cont):
            print('N')
        else:
            print('Y')

    N, B = map(int, input().split())

