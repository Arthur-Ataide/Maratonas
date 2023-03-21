while(1):
    num = int(input())

    if num == 0:
        break

    a = []
    dif = 1
    nao = 1

    for i in range(num):
        pal = list(input())
        b = sorted(pal)
        b = ''.join(b)
        a.append(b)

    veri = 0
    i = 1

    while(1):
        
        if (a[veri] != a[i]):
            i += 1

        else:
            del a[i]
        r = len(a)
        if i == r and r-1 != veri:
            i = veri + 2
            veri += 1
        
        if veri == r-1:
            break

    print(r)
        