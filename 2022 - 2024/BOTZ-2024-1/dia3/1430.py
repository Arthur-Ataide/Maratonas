W = 64
H = 32
Q = 16
E = 8
S = 4
T = 2
X = 1

while(1):
    l = input()
    totCo = 0
    tot = 0

    for i in l:

        if i == '*':
            # print()
            exit()

        elif i == 'W':
            tot += W

        elif i == 'H':
            tot += H

        elif i == 'Q':
            tot += Q
            
        elif i == 'E':
            tot += E
            
        elif i == 'S':
            tot += S
            
        elif i == 'T':
            tot += T
            
        elif i == 'X':
            tot += X

        elif i == '/':
            if tot == 64:
                totCo += 1
            tot = 0
            

    if (l[0] != '/'):
        if tot == 64:
            totCo += 1
            tot = 0

    print(totCo)
    totCo = 0
            

            
    
# /HH/QQQQ/XXXTXTEQH/W/HW/
# /W/W/SQHES/
# /WE/TEX/THES/
# * 
