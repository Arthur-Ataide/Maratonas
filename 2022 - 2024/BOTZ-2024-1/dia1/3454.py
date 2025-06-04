p, s, t = list(input().upper())

O = 0

if (p == "O"):
    O += 1
    
if (s == "O"):
    O += 1
    
if (t == "O"):
    O += 1


if(O != 1):
    print("?")
    
elif(p == "X" and s=="X"):
    print("Alice")
    
elif(s=="X" and t=="X"):
    print("Alice")
else:
    print("*")