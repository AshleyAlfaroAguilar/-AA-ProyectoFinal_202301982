#AUTOR: ASHLEY DAYANE ALFARO AGUILAR 
"""
Implementación del algoritmo de Prim para Árbol de Expansión Mínima (MST).

Genera el archivo PNG: prim_mst.png
"""

import csv
import heapq
from typing import Dict, List, Tuple, Set

import matplotlib.pyplot as plt
import networkx as nx


def cargar_grafo_csv(ruta_csv: str) -> Tuple[Set[str], List[Tuple[str, str, float]], Dict[str, List[Tuple[str, float]]]]:
    """Carga un grafo no dirigido y ponderado desde un archivo CSV.

    El CSV debe tener encabezados: origen,destino,peso

    Returns:
        vertices: conjunto de nodos.
        aristas: lista de aristas (u, v, peso).
        adyacencia: lista de adyacencia para cada vértice.
    """
    vertices: Set[str] = set()
    aristas: List[Tuple[str, str, float]] = []
    adyacencia: Dict[str, List[Tuple[str, float]]] = {}

    with open(ruta_csv, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            u = fila["origen"].strip()
            v = fila["destino"].strip()
            w = float(fila["peso"])
            vertices.update([u, v])
            aristas.append((u, v, w))

            adyacencia.setdefault(u, []).append((v, w))
            adyacencia.setdefault(v, []).append((u, w))

    return vertices, aristas, adyacencia


def prim_mst(adyacencia: Dict[str, List[Tuple[str, float]]], inicio: str) -> List[Tuple[str, str, float]]:
    """Aplica el algoritmo de Prim para obtener el MST.

    Args:
        adyacencia: diccionario de listas (nodo -> [(vecino, peso), ...]).
        inicio: nodo inicial.

    Returns:
        Lista de aristas (u, v, peso) que conforman el MST.

    Complejidad:
        Usando cola de prioridad (heap), O(E log V), donde
        E es el número de aristas y V el número de vértices.
    """
    visitados: Set[str] = set([inicio])
    mst: List[Tuple[str, str, float]] = []
    heap: List[Tuple[float, str, str]] = []  # (peso, u, v)

    for v, w in adyacencia.get(inicio, []):
        heapq.heappush(heap, (w, inicio, v))

    while heap and len(visitados) < len(adyacencia):
        w, u, v = heapq.heappop(heap)
        if v in visitados:
            continue
        visitados.add(v)
        mst.append((u, v, w))

        for vecino, peso in adyacencia.get(v, []):
            if vecino not in visitados:
                heapq.heappush(heap, (peso, v, vecino))

    return mst


def dibujar_mst(vertices: Set[str], mst: List[Tuple[str, str, float]], nombre_archivo: str) -> None:
    """Dibuja el MST utilizando networkx y lo guarda como PNG."""
    g = nx.Graph()
    g.add_nodes_from(vertices)
    for u, v, w in mst:
        g.add_edge(u, v, weight=w, label=str(w))

    pos = nx.spring_layout(g)

    plt.figure()
    nx.draw(g, pos, with_labels=True)
    etiquetas = nx.get_edge_attributes(g, "weight")
    nx.draw_networkx_edge_labels(g, pos, edge_labels=etiquetas)
    plt.title("Árbol de Expansión Mínima (Prim)")
    plt.tight_layout()
    plt.savefig(nombre_archivo)
    plt.close()

    print(f"[OK] Imagen MST de Prim guardada en {nombre_archivo}")


def ejecutar_prim(ruta_csv: str) -> None:
    """Función de alto nivel que carga el grafo, ejecuta Prim y genera el PNG."""
    print("\n=== Ejecutando Prim ===")
    vertices, _, adyacencia = cargar_grafo_csv(ruta_csv)
    if not vertices:
        print("El grafo está vacío.")
        return

    inicio = next(iter(vertices))  # Tomamos cualquier nodo como inicial
    mst = prim_mst(adyacencia, inicio)

    print("Aristas del MST (Prim):")
    for u, v, w in mst:
        print(f"{u} - {v} (peso {w})")

    dibujar_mst(vertices, mst, "prim_mst.png")
