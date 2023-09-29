a = input()
b = input()

c = len(a)
d = len(b)

if (c == d):
    print("")

elif (len(a) > len(b)):
    for i in range(c-d-1):
        print("1", end="")
    print("1")
else:
    print("-", end="")
    for i in range(d-c-1):
        print("1", end="")
    print("1")

