n = int(input())

def gera(x):
    b = bin(x)[2:]
    
    if b == b[::-1]:
        return int(b, 2)
    
    return 

while(1):
    v = gera(n)
    if v:
        print(v)
        break
    n-=1