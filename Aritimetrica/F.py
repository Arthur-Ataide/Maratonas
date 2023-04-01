a = input().split()
mdc = int(a[0])
d = len(a)

for c in range(d):
    e = int(a[c])

    if mdc % e == 0 or e % mdc == 0:
        if mdc > e:
            mdc = e
    
    else:
        if mdc > e:
            for i in range(e//2, 0, -1):
                if(mdc % i == 0 and e % i == 0):
                    mdc = i
                # print(e//2)
        
        else:
            for i in range(mdc//2, 0, -1):
                if(mdc % i == 0 and e % i== 0):
                    mdc = i
                    # print(mdc//2)


print(mdc)