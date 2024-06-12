def primo(n):
    if n == 1:
        return True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return True
    return False

def menor_maior(vetor):
    vetor[1] = vetor[1] + 1
    return vetor

def continua(vetor):
    vetor[0] = vetor[0] - 1
    vetor[1] = vetor[1] + 1
    
num = int(input())

for i in range(num):
    impar = int(input())
    
    sobre2 = impar // 2
    vetor = [sobre2, sobre2] # [menor, maior]
    
    cont = 1
    vetor = menor_maior(vetor)
    if primo(vetor[0]) and primo(vetor[1]) and vetor[0] > 0:
        print(vetor[0], vetor[1])
        
    else:
        while vetor[0] > 1:
            continua(vetor)
            if primo(vetor[0]) and primo(vetor[1]) and vetor[0] > 0:
                print(vetor[0], vetor[1])
                cont = 0
                break
                
        if (cont):
            print(-1)
        
            
    
    