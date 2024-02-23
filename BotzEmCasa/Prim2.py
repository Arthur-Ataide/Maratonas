import heapq

def prim(graph, start):
    # Inicialização de variáveis
    mst = []
    visited = set()
    heap = [(0, start)]

    while heap:
        # Obtém a aresta de menor peso
        weight, current_vertex = heapq.heappop(heap)

        # Se o vértice já foi visitado, continue
        if current_vertex in visited:
            continue
        
        # Adiciona o vértice à MST
        mst.append((current_vertex, weight))
        visited.add(current_vertex)

        # Adiciona as arestas adjacentes ao heap
        for neighbor, edge_weight in graph[current_vertex]:
            if neighbor not in visited:
                heapq.heappush(heap, (edge_weight, neighbor))

    return mst

def main():
    # Entrada do usuário: número de vértices e arestas
    num_vertices = int(input("Digite o número de vértices: "))
    num_edges = int(input("Digite o número de arestas: "))

    # Inicializa o grafo como um dicionário de listas de adjacência
    graph = {i: [] for i in range(1, num_vertices + 1)}

    # Entrada do usuário: arestas e pesos
    for _ in range(num_edges):
        v1, v2, weight = map(int, input("Digite a aresta (v1 v2 peso): ").split())
        graph[v1].append((v2, weight))
        graph[v2].append((v1, weight))

    # Escolhe um vértice inicial (poderia ser qualquer vértice)
    start_vertex = int(input("Digite o vértice inicial: "))

    # Executa o algoritmo de Prim
    minimum_spanning_tree = prim(graph, start_vertex)

    cont = 0
    # Imprime a Árvore Geradora Mínima
    print("Árvore Geradora Mínima:")
    for vertex, weight in minimum_spanning_tree:
        cont += weight

    print(cont)
    
if __name__ == "__main__":
    main()