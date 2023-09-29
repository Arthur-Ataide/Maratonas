a = int(input())

primo = 1

while (True):
    
        
    for i in range(2,(a//2)+1):
        if (a % i == 0):
            primo = 0
            break

    if primo == 1:
        a += 1
        for i in range(2,(a//2)+1):
            if (a % i == 0):
                primo = 0
                break

        if primo == 0:
            primo = 1
            a += 1
            for i in range(2,(a//2)+1):
                if (a % i == 0):
                    primo = 0
                    break
            if primo == 1:
                print(a-1)
                exit()
            else:
                a -= 1
    else:
         a+=1
    primo = 1

        