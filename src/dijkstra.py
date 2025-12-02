#AUTOR: ASHLEY DAYANE ALFARO AGUILAR 
"""
Implementación del algoritmo de Dijkstra para rutas más cortas.

Genera el archivo PNG: dijkstra_paths.png
"""

import csv
import heapq
from typing import Dict, List, Tuple, Set

import matplotlib.pyplot as plt
import networkx as nx


def cargar_grafo_csv(ruta_csv: str) -> Tuple[Set[str], Dict[str, List[Tuple[str, float]]]]:
    """Carga un grafo no dirigido y ponderado desde CSV.

    Returns:
        vertices: conjunto de nodos.
        adyacencia: diccionario de listas (u -> [(v, peso), ...]).
    """
    vertices: Set[str] = set()
    adyacencia: Dict[str, List[Tuple[str, float]]] = {}

    with open(ruta_csv, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            u = fila["origen"].strip()
            v = fila["destino"].strip()
            w = float(fila["peso"])
            vertices.update([u, v])
            adyacencia.setdefault(u, []).append((v, w))
            adyacencia.setdefault(v, []).append((u, w))

    return vertices, adyacencia


def dijkstra(adyacencia: Dict[str, List[Tuple[str, float]]], origen: str) -> Tuple[Dict[str, float], Dict[str, str]]:
    """Aplica Dijkstra para obtener distancias mínimas y predecesores.

    Args:
        adyacencia: lista de adyacencia.
        origen: nodo origen.

    Returns:
        dist: distancias mínimas desde origen.
        prev: predecesor de cada nodo en el camino más corto.

    Complejidad:
        Usando cola de prioridad, O(E log V).
    """
    dist = {v: float("inf") for v in adyacencia}
    prev: Dict[str, str] = {}
    dist[origen] = 0.0

    heap: List[Tuple[float, str]] = [(0.0, origen)]

    while heap:
        d_actual, u = heapq.heappop(heap)
        if d_actual > dist[u]:
            continue

        for v, w in adyacencia.get(u, []):
            nuevo = dist[u] + w
            if nuevo < dist[v]:
                dist[v] = nuevo
                prev[v] = u
                heapq.heappush(heap, (nuevo, v))

    return dist, prev


def reconstruir_camino(prev: Dict[str, str], origen: str, destino: str) -> List[str]:
    """Reconstruye el camino más corto desde origen hasta destino usando prev."""
    camino = [destino]
    while destino in prev and destino != origen:
        destino = prev[destino]
        camino.append(destino)
    camino.reverse()
    if camino and camino[0] == origen:
        return camino
    return []


def dibujar_caminos(
    vertices: Set[str],
    adyacencia: Dict[str, List[Tuple[str, float]]],
    origen: str,
    prev: Dict[str, str],
    nombre_archivo: str,
) -> None:
    """Dibuja el grafo resaltando los caminos mínimos desde el origen."""
    g = nx.Graph()
    for u in vertices:
        g.add_node(u)
        for v, w in adyacencia.get(u, []):
            if not g.has_edge(u, v):
                g.add_edge(u, v, weight=w)

    pos = nx.spring_layout(g)

    plt.figure()
    nx.draw(g, pos, with_labels=True)

    # Resaltar aristas que pertenecen a algún camino mínimo
    aristas_resaltadas = []
    for nodo in vertices:
        if nodo == origen:
            continue
        camino = reconstruir_camino(prev, origen, nodo)
        for i in range(len(camino) - 1):
            u, v = camino[i], camino[i + 1]
            if (u, v) not in aristas_resaltadas and (v, u) not in aristas_resaltadas:
                aristas_resaltadas.append((u, v))

    nx.draw_networkx_edges(
        g,
        pos,
        edgelist=aristas_resaltadas,
        width=3,
    )

    etiquetas = nx.get_edge_attributes(g, "weight")
    nx.draw_networkx_edge_labels(g, pos, edge_labels=etiquetas)
    plt.title(f"Caminos mínimos desde {origen} (Dijkstra)")
    plt.tight_layout()
    plt.savefig(nombre_archivo)
    plt.close()

    print(f"[OK] Imagen de rutas Dijkstra guardada en {nombre_archivo}")


def ejecutar_dijkstra(ruta_csv: str, origen: str) -> None:
    """Función de alto nivel que carga el grafo, ejecuta Dijkstra y genera el PNG."""
    print("\n=== Ejecutando Dijkstra ===")
    vertices, adyacencia = cargar_grafo_csv(ruta_csv)
    if origen not in vertices:
        print(f"El nodo origen '{origen}' no existe en el grafo. Nodos disponibles: {sorted(vertices)}")
        return

    dist, prev = dijkstra(adyacencia, origen)

    print(f"Distancias mínimas desde {origen}:")
    for v in sorted(dist):
        print(f"{origen} -> {v}: {dist[v]}")

    for v in sorted(vertices):
        if v == origen:
            continue
        camino = reconstruir_camino(prev, origen, v)
        if camino:
            print(f"Camino más corto a {v}: {' -> '.join(camino)}")

    dibujar_caminos(vertices, adyacencia, origen, prev, "dijkstra_paths.png")
