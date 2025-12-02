"""AUTOR: ASHLEY DAYANE ALFARO AGUILAR
Implementación del algoritmo de Huffman para codificación óptima.

Genera:
- huffman_tree.png
- huffman_freq.png
"""

import heapq
from collections import Counter
from dataclasses import dataclass
from typing import Dict, Optional, List

import matplotlib.pyplot as plt
import networkx as nx


@dataclass
class NodoHuffman:
    """Nodo del árbol de Huffman.

    Se define __lt__ para que heapq compare solo por frecuencia.
    """

    frecuencia: int
    caracter: Optional[str] = None
    izquierda: Optional["NodoHuffman"] = None
    derecha: Optional["NodoHuffman"] = None

    def __lt__(self, other: "NodoHuffman") -> bool:
        """Permite comparar nodos por frecuencia en heapq.

        Complejidad: O(1)
        """
        return self.frecuencia < other.frecuencia


def leer_texto(ruta_txt: str) -> str:
    """Lee el contenido completo de un archivo de texto."""
    with open(ruta_txt, encoding="utf-8") as f:
        return f.read()


def construir_arbol_huffman(texto: str) -> Optional[NodoHuffman]:
    """Construye el árbol de Huffman a partir de un texto.

    Complejidad:
        O(n log k), donde n es la longitud del texto y k el número
        de símbolos distintos.
    """
    if not texto:
        return None

    frecuencias = Counter(texto)
    heap: List[NodoHuffman] = [NodoHuffman(freq, char) for char, freq in frecuencias.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        nodo1 = heapq.heappop(heap)
        nodo2 = heapq.heappop(heap)
        combinado = NodoHuffman(nodo1.frecuencia + nodo2.frecuencia, None, nodo1, nodo2)
        heapq.heappush(heap, combinado)

    return heap[0]


def generar_codigos(
    nodo: Optional[NodoHuffman],
    prefijo: str = "",
    codigos: Optional[Dict[str, str]] = None,
) -> Dict[str, str]:
    """Genera la tabla de códigos de Huffman recorriendo el árbol."""
    if codigos is None:
        codigos = {}

    if nodo is None:
        return codigos

    if nodo.caracter is not None:
        # Caso hoja: asignamos el código actual
        codigos[nodo.caracter] = prefijo or "0"
    else:
        generar_codigos(nodo.izquierda, prefijo + "0", codigos)
        generar_codigos(nodo.derecha, prefijo + "1", codigos)

    return codigos


def representacion_textual_arbol(nodo: Optional[NodoHuffman], prefijo: str = "") -> str:
    """Genera una representación textual del árbol de Huffman (preorden)."""
    if nodo is None:
        return ""

    if nodo.caracter is not None:
        return f"{prefijo}Hoja: '{repr(nodo.caracter)[1:-1]}' (freq={nodo.frecuencia})\n"

    texto = f"{prefijo}Nodo interno (freq={nodo.frecuencia})\n"
    texto += representacion_textual_arbol(nodo.izquierda, prefijo + "  ")
    texto += representacion_textual_arbol(nodo.derecha, prefijo + "  ")
    return texto


def dibujar_frecuencias(texto: str, nombre_archivo: str) -> None:
    """Dibuja un gráfico de barras con las frecuencias de cada carácter."""
    frecuencias = Counter(texto)
    caracteres = list(frecuencias.keys())
    valores = [frecuencias[c] for c in caracteres]

    plt.figure(figsize=(10, 4))
    plt.bar(range(len(caracteres)), valores)
    # Mostramos los caracteres con repr para distinguir espacios, saltos, etc.
    plt.xticks(range(len(caracteres)), [repr(c)[1:-1] for c in caracteres], rotation=90)
    plt.title("Frecuencias de caracteres (Huffman)")
    plt.tight_layout()
    plt.savefig(nombre_archivo)
    plt.close()

    print(f"[OK] Imagen de frecuencias de Huffman guardada en {nombre_archivo}")


def dibujar_arbol(nodo: Optional[NodoHuffman], nombre_archivo: str) -> None:
    """Dibuja el árbol de Huffman como un grafo y lo guarda en PNG."""
    if nodo is None:
        print("No hay árbol para dibujar.")
        return

    g = nx.DiGraph()

    def agregar_nodos(n: NodoHuffman, nombre: str):
        # Si es hoja, mostramos carácter y frecuencia; si no, solo frecuencia
        etiqueta = f"{repr(n.caracter)[1:-1]}\n{n.frecuencia}" if n.caracter is not None else str(n.frecuencia)
        g.add_node(nombre, label=etiqueta)
        if n.izquierda:
            hijo_izq = nombre + "0"
            agregar_nodos(n.izquierda, hijo_izq)
            g.add_edge(nombre, hijo_izq, label="0")
        if n.derecha:
            hijo_der = nombre + "1"
            agregar_nodos(n.derecha, hijo_der)
            g.add_edge(nombre, hijo_der, label="1")

    agregar_nodos(nodo, "root")

    # Usamos spring_layout para evitar dependencias externas (Graphviz, etc.)
    pos = nx.spring_layout(g)

    plt.figure(figsize=(8, 6))
    nx.draw(g, pos, with_labels=False, arrows=True)
    etiquetas_nodos = nx.get_node_attributes(g, "label")
    nx.draw_networkx_labels(g, pos, labels=etiquetas_nodos, font_size=8)
    etiquetas_aristas = nx.get_edge_attributes(g, "label")
    nx.draw_networkx_edge_labels(g, pos, edge_labels=etiquetas_aristas, font_size=8)
    plt.title("Árbol de Huffman")
    plt.tight_layout()
    plt.savefig(nombre_archivo)
    plt.close()

    print(f"[OK] Imagen del árbol de Huffman guardada en {nombre_archivo}")


def ejecutar_huffman(ruta_txt: str) -> None:
    """Función de alto nivel que lee el texto, ejecuta Huffman y genera PNGs."""
    print("\n=== Ejecutando Huffman ===")
    texto = leer_texto(ruta_txt)
    if not texto:
        print("El archivo de texto está vacío.")
        return

    arbol = construir_arbol_huffman(texto)
    codigos = generar_codigos(arbol)

    print("Tabla de códigos de Huffman (carácter -> código):")
    for caracter, codigo in codigos.items():
        print(f"{repr(caracter)[1:-1]} -> {codigo}")

    print("\nRepresentación textual del árbol:")
    print(representacion_textual_arbol(arbol))

    dibujar_frecuencias(texto, "huffman_freq.png")
    dibujar_arbol(arbol, "huffman_tree.png")
