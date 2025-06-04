a = int(input())

m = [0 for i in range(a)]
erro = []

b = input().split()

soma = 0
foi = 0

for i in range(a):
    soma += int(b[i])
    b[i] = int(b[i])
    if i != a-1:
        if b[i] == b[i+1]:
            foi+=1
        
if foi == a:
    print(soma)
    exit()



foi = 0 
cont = 0

while(True):
    
    for i in range(a-1):
        
        if i == 0:
            m[a-1] = abs(b[i] - b[a-1])
            soma += m[a-1]
            
        m[i] = abs(b[i] - b[i+1])
        soma += m[i]    
        b[i] = m[i]
        
    for i in range(a):
        if m[0] == m[i]:
            foi += 1
                   
    if foi == a:
        print(soma)
        exit()
    
    
    cont += 1
    b[a-1] = m[a-1]
    foi = 0
    
    
    if cont == 500:
        erro = m[:]
    
    if cont != 500 and erro == m:
        print(-1)
        exit()
    
    
    
        