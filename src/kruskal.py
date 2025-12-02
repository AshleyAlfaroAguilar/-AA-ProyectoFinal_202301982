"""AUTOR: ASHLEY DAYANE ALFARO AGUILAR  
Implementación del algoritmo de Kruskal para Árbol de Expansión Mínima (MST).

Genera el archivo PNG: kruskal_mst.png
"""

import csv
from typing import Dict, List, Tuple, Set

import matplotlib.pyplot as plt
import networkx as nx


def cargar_grafo_csv(ruta_csv: str) -> Tuple[Set[str], List[Tuple[str, str, float]]]:
    """Carga un grafo no dirigido y ponderado desde un archivo CSV.

    Returns:
        vertices: conjunto de nodos.
        aristas: lista de aristas (u, v, peso).
    """
    vertices: Set[str] = set()
    aristas: List[Tuple[str, str, float]] = []

    with open(ruta_csv, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            u = fila["origen"].strip()
            v = fila["destino"].strip()
            w = float(fila["peso"])
            vertices.update([u, v])
            aristas.append((u, v, w))

    return vertices, aristas


class UnionFind:
    """Estructura Union-Find (Disjoint Set Union) para Kruskal.

    Complejidad:
        Operaciones casi O(1) amortizado usando path compression
        y union by rank.
    """

    def __init__(self, elementos):
        self.padre = {e: e for e in elementos}
        self.rango = {e: 0 for e in elementos}

    def encontrar(self, x):
        """Encuentra el representante del conjunto de x (con path compression)."""
        if self.padre[x] != x:
            self.padre[x] = self.encontrar(self.padre[x])
        return self.padre[x]

    def unir(self, x, y):
        """Une los conjuntos de x e y."""
        rx, ry = self.encontrar(x), self.encontrar(y)
        if rx == ry:
            return False
        if self.rango[rx] < self.rango[ry]:
            self.padre[rx] = ry
        elif self.rango[rx] > self.rango[ry]:
            self.padre[ry] = rx
        else:
            self.padre[ry] = rx
            self.rango[rx] += 1
        return True


def kruskal_mst(vertices: Set[str], aristas: List[Tuple[str, str, float]]) -> List[Tuple[str, str, float]]:
    """Aplica el algoritmo de Kruskal para obtener el MST.

    Args:
        vertices: conjunto de nodos.
        aristas: lista de aristas (u, v, peso).

    Returns:
        Lista de aristas del MST.

    Complejidad:
        Dominado por el ordenamiento de aristas: O(E log E) ≈ O(E log V).
    """
    uf = UnionFind(vertices)
    mst: List[Tuple[str, str, float]] = []

    aristas_ordenadas = sorted(aristas, key=lambda x: x[2])

    for u, v, w in aristas_ordenadas:
        if uf.unir(u, v):
            mst.append((u, v, w))

    return mst


def dibujar_mst(vertices: Set[str], mst: List[Tuple[str, str, float]], nombre_archivo: str) -> None:
    """Dibuja el MST resultante de Kruskal y lo guarda en PNG."""
    g = nx.Graph()
    g.add_nodes_from(vertices)
    for u, v, w in mst:
        g.add_edge(u, v, weight=w)

    pos = nx.spring_layout(g)

    plt.figure()
    nx.draw(g, pos, with_labels=True)
    etiquetas = nx.get_edge_attributes(g, "weight")
    nx.draw_networkx_edge_labels(g, pos, edge_labels=etiquetas)
    plt.title("Árbol de Expansión Mínima (Kruskal)")
    plt.tight_layout()
    plt.savefig(nombre_archivo)
    plt.close()

    print(f"[OK] Imagen MST de Kruskal guardada en {nombre_archivo}")


def ejecutar_kruskal(ruta_csv: str) -> None:
    """Función de alto nivel que carga el grafo, ejecuta Kruskal y genera el PNG."""
    print("\n=== Ejecutando Kruskal ===")
    vertices, aristas = cargar_grafo_csv(ruta_csv)
    if not vertices:
        print("El grafo está vacío.")
        return

    mst = kruskal_mst(vertices, aristas)

    print("Aristas del MST (Kruskal):")
    for u, v, w in mst:
        print(f"{u} - {v} (peso {w})")

    dibujar_mst(vertices, mst, "kruskal_mst.png")
