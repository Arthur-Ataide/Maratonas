Vet = ['a','b','c','d','e','f','g','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

a = input()
for c in range(26):
    if Vet[c] not in a:
        print(Vet[c])
        exit()