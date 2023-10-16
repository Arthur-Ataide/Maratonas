vet = []

a = input()
while(a != EOFError):
    vet.append(a)
    a = input()

vet.sort()
print(vet)
for c in vet:
    print(c)