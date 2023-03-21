a , b = input().split(" ")
a = list(a)
b = list(b)
cond = 1
i = 0


while cond == 1:
    if len(b)==0 or i >= len(a):
        cond = 2
        break
    
    # print(len(b), b ,  len(a), i)
    # print(a[i], a)
    
    r = (''.join(b)).find(a[i])
    
    # print(r)
    
    if r==-1:
        cond = 0
    else:
        for j in range(r+1):
            # print(b)
            del b[0]
            
        # print("ttex", ''.join(b))
        i += 1


if cond == 2:     
    print("sim")
if cond == 0:
    print("nao")