frase = input().split()

for i in range(len(frase)):
    for j in range(len(frase[i])):
        if j % 2 != 0:
            print(frase[i][j], end='')
    if i != len(frase) - 1:
        print(end=' ')
print()