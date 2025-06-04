
def mdc(x, y):
    resto = 0
    while True:
        resto = x % y
        
        x = y
        y = resto
        if(resto == 0):
            break
    return x
    

y, k = map(int, input().split())
x = 1
for i in range(k):
    print(x, y, k-i)
    x = x + mdc(x, y)

print(x)
