a,b,c = input().split()
d = ((int(b)**2) -4*int(a)*int(c))**(1/2)
try:
    d = float(d)
    x1 = (-int(b) -d) / (2*int(a))
    x2 = (-int(b) +d) / (2*int(a))
    print("{:.2f} {:.2f}".format(x2,x1))
except:
    print("Nulo")