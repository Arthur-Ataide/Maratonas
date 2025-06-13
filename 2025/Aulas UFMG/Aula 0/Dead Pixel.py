n = int((input()))


for i in range(n):
    a,b,x,y = map(int, input().split())
    x+=1
    y+=1
    
    print(max(b*(a-x), b*(x-1), a*(b-y), a*(y-1)))
    
    