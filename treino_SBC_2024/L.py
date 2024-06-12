def ultimoMenorAtual(atual, tam, quarto):
    if (quarto == atual):
        print((str(atual) + " ") * (tam-1), end='')
        print(atual)
        exit()

def printConsecutivo(atual, num, quartos, quarto):
    
    ultimoMenorAtual(atual, num - i, quarto)
    
    try:
        cont = quartos.index(atual)
    except ValueError:
        return -1
    
    print((str(atual) + ' ') * (cont + 1), end='')
    return cont + 1


num = int(input())

quartos = input().split()

idade = input().split()

cont = 0
quarto = quartos[num-1]

i = 0
rep = 0


while (i < num):
    aux = printConsecutivo(idade[cont], num, quartos[i:num], quarto)
    
    cont += 1
    
    if (aux != -1):
        i += aux
        

# 5
# Alice Bob Dora Eve Clara
# Clara Dora Eve Bob Alice



