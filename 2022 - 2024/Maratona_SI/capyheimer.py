Q = int(input())
for c in range(Q):
    T, B, N = input().split()
    T = int(T)
    N = int(N)
    valor = N
    total = N
    
    while(1):
        valor = valor * 2
        total = total + valor
        
        if total > T:
            if T - (total - valor) >=  valor//2:
                print(T - (total - valor))
                break
            
            if total - valor == T or T - (total - valor) <  valor//2:
                print(valor//2)
                break