a = [0, 1, 2]
b = a[:]

b[1] = 2

if a != b:
    print(a)
    print("oi")
else:   
    print(b)