a = list(input())
b = list(input())

a.sort()
b.sort()
Erro = 1
if len(a) == len(b):
    for i in range(len(a)):
        if a[i] != b[i]:
            Erro = 0
            break
        
else:
    Erro = 0

print(Erro)
# iracema
# america