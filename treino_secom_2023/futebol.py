total = 0

for i in range(11):
    esq, dir = map(int, input().split())
    total += esq + dir
 
if total%11 == 0:
    print(11)
    exit()
    
print((total%11))