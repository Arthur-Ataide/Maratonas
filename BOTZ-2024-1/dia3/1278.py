tam = int(input())

if(tam == 0):
    exit()

while(1):
    
    

    vet = []
    maior = 0

    for i in range(tam):
        linha = input().split()
        aux = ''

        for j in linha:
            if (len(aux) > 0):
                aux += " " + j
            else: 
                aux += j
        
        vet.append(aux)

        if (maior < len(aux)):
            maior = len(aux)

    for i in vet:
 
        aux = str(i).zfill(maior)
        print(aux.replace('0', ' '))
    
    tam = int(input())
    if(tam == 0):
        exit()
    print()
    


# vet = ['oi', 'tudo', 'bem']

        
