matriz = [1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
N = int(input())
ans = 1
cont = 0
while N >= matriz[cont]:
    ans *= matriz[cont]
    cont += 1
while True:
    aux = 0
    for c in range(1,N+1):
        if ans % c != 0:
            aux = 1
            continue
    if aux == 0:
        print(ans)
        exit()
    else:
        ans += 1
        