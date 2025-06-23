import heapq
from math import inf
from typing import Dict, Hashable, Tuple

def dijkstra(graph: Dict[Hashable, Dict[Hashable, float]],
             source: Hashable) -> Tuple[Dict[Hashable, float],
                                        Dict[Hashable, Hashable]]:
    """
    Calcola le distanze minime da `source` a tutti i nodi in un grafo
    rappresentato come:
        graph[u] = {v1: peso1, v2: peso2, ...}
    Restituisce:
        dist  – dizionario nodo -> distanza minima
        prev  – dizionario nodo -> predecessore sul cammino minimo (None per source)
    Richiede: pesi non negativi.
    """
    dist: Dict[Hashable, float] = {node: inf for node in graph}
    prev: Dict[Hashable, Hashable] = {node: None for node in graph}
    dist[source] = 0

    heap: list[Tuple[float, Hashable]] = [(0, source)]  # (distanza, nodo)

    while heap:
        d_u, u = heapq.heappop(heap)
        if d_u > dist[u]:          # record obsoleto
            continue

        for v, weight in graph[u].items():
            alt = d_u + weight
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(heap, (alt, v))

    return dist, prev

g = {
    'A': {'B': 5, 'C': 1},
    'B': {'C': 2, 'D': 1},
    'C': {'B': 3, 'D': 4, 'E': 8},
    'D': {'E': 2},
    'E': {}
}

dist, prev = dijkstra(g, 'A')
print("Distanze minime da A:", dist)
# Output atteso (pesi totali):
# {'A': 0, 'B': 4, 'C': 1, 'D': 5, 'E': 7}