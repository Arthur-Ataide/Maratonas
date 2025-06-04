cont = 0
while(1): 
    
    maximo, rua = map(int, input().split())
    cont +=1

    if (maximo == 0 and rua == 0):
        exit()
    
    else:
        div = maximo/rua

        if (maximo % rua == 0):
            div -=1

        if(div <= 27):
            print(f'Case {cont}: {int(div)}')

        else:
            print(f'Case {cont}: impossible')
