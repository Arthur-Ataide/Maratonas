vertice, aresta = map(int, input().split())

grafo = [[] for i in range(vertice+1)]
grafoPesos = [[] for i in range(vertice+1)]
visitado = [[] for i in range(vertice+1)]


for i in range(aresta):
    a, b, peso = map(int, input().split())
    grafo[a].append(b)
    grafo[b].append(a)
    grafoPesos[a].append(peso)
    grafoPesos[b].append(peso)
    visitado[a].append(False)
    visitado[b].append(False)

visitado[0] = True
custo = 0

verVisitado = [False for i in range(vertice+1)]
verVisitado[0] = True

print(grafo)
print(grafoPesos)
atual = 1

print(visitado)
print(verVisitado)

while False in verVisitado:
    # print("oi")
    menor = 1001
    # print("visitado = ",visitado)
    for i in r
        # if (grafo[atual] != []):
        pos = atual
        anterior = atual
        print("vertice atual = ",atual)
        
        for j in range(0, len(grafo[atual])):
            print("comparando com =",grafo[atual][j])
            if grafoPesos[atual][j] < menor and visitado[grafo[atual][j]] == False:
                menor = grafoPesos[atual][j]
                pos = grafo[atual][j]
                # vertice = i
        if (menor != 1001):
            custo += menor
            print("o menor = ",pos)
            print("menor valor achado = ",menor)
        visitado[atual][pos] = True
        visitado[pos][atual] = True
        verVisitado[atual] = True
        # verVisitado[pos] = True
        atual = pos
        
        print("atual = ",atual)
            
            
# while False in visitado:
#     atual = 1
#     if (grafo[atual] == [] or visitado[atual] == True or grafoPesos[atual] == []):
#         pos = atual+1
        
#     # nao passar do tamanho do grafo
#     # print(len(grafo))
#     if (pos > vertice):
#         break
        
#     for i in range(1, len(grafo[atual])):
#         if grafoPesos[atual][i] < menor:
#             menor = grafoPesos[atual][i]
#             pos = i
#             # vertice = i
#     custo += menor
#     visitado[pos] = True
#     grafo[atual].pop(pos)
#     grafoPesos[atual].pop(pos)

print(custo)

