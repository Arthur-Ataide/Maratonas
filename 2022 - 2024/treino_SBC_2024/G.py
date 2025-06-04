def fim(distancia):
    if K >= distancia:
        return 1
    return 0

def caminho(chegada, tabaco, distancia):
    if distancia + tabaco >= chegada:
        return 1
    return 0

def progdinamica(atual, parou):
    if fim(dist[atual]):
        vetParou.append(parou)

    for i in range(atual-1, -1, -1):
        if caminho(dist[atual], tabaco[i], dist[i]):
            parou += 1
            progdinamica(i, parou)
            parou -= 1

N, K = map(int, input().split())

dist = list(map(int, input().split()))
tabaco = list(map(int, input().split()))

percorrer = dist[N-1]
parou = 0
vetParou = []

progdinamica(N-1, parou)
vetParou.sort()

try:
    print(vetParou[0])
except:
    print(-1)   
