a = int(input())
v = []

while(a != EOFError):
    

    if a % 2 != 0:
        if a in v:
            a = 2
        else:
            v.append(a)
    a = int(input())

v.sort()
for i in range(len(v)):
    print(v[i])

        

