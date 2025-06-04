# facil

n = int(input())

if n == 1:
    print("nao")
    exit(0)
for i in range(2, int(n**(1/2))):
    if i % n == 0:
        print("nao")
        exit(0)

print("sim")