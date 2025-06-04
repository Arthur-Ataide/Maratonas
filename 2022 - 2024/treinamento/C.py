def printMatrix(matrix):
    print()
    for i in range(linha):
        for j in range(coluna):
            print(matrix[i][j], end='')
        print()
        
def procura(x, y, matrix, cont, entra):    
    vetX = [1, 1, 0, 1, 0, -1, -1, -1]
    vetY = [0, 1, 1, -1, -1, 0, 1, -1]
    
    if (matrix[x][y] == '#'):
        if entra:
            cont += 1
            entra = 0
    
        matrix[x][y] = cont
    
        # printMatrix(matrix)
        for c in range(8):
            # print()
            # print(x+vetX[c], y+vetY[c])
            if(0 <= x + vetX[c] < linha and 0 <= y + vetY[c] < coluna):
                # print(x+vetX[c], y+vetY[c])
                
                if matrix[x+vetX[c]][y+vetY[c]] == '#':
                    procura(x+vetX[c], y+vetY[c], matrix, cont, entra)
        # for c in range(8):
        #         if(0 <= i+vetX[c] < linha and 0 <= j+vetX[c] < coluna):
        #             print(matrix[i+vetX[c]][j+vetY[c]])

    return cont
    
linha, coluna = map(int, input().split())
matrix = []

for i in range(linha):
    a = input()

    matrix.append(list(a))

cont = 0
entra = 1
# procura(0, 1, matrix, cont, entra)

for i in range(linha):
    for j in range(coluna):
        entra = 1
        cont = procura(i, j, matrix, cont, entra)

print(cont)
