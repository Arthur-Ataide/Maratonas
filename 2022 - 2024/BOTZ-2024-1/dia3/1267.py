coluna, linha = map(int, input().split())

while(1):
    if (linha == 0 and coluna == 0):
        exit()
    
    alunos = [0 for i in range(coluna)]
    for i in range(linha):
        x = input().split()
        # zeros = []
        
        while('0' in x):
            indice = x.index('0')
            alunos[indice] = 1
            x[indice] = 2


    if (0 in alunos):
        print('yes')
    else: 
        print('no')
    
    coluna, linha = map(int, input().split())

# x = ['1', '2', '3']

# print(x.index('2'))
