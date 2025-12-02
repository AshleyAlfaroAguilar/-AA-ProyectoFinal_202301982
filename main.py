"""Autor: ASHLEY DAYANE ALFARO AGUILAR
Punto de entrada del Proyecto Final de Algoritmos Avanzados.

Contiene el menú interactivo para ejecutar:
- Prim
- Kruskal
- Dijkstra
- Huffman
"""

from src.prim import ejecutar_prim
from src.kruskal import ejecutar_kruskal
from src.dijkstra import ejecutar_dijkstra
from src.huffman import ejecutar_huffman


def mostrar_menu() -> None:
    """Muestra el menú principal en consola."""
    print("\n=== PROYECTO FINAL: ALGORITMOS AVANZADOS ===")
    print("0. Salir")
    print("1. Ejecutar Prim")
    print("2. Ejecutar Kruskal")
    print("3. Ejecutar Dijkstra")
    print("4. Ejecutar Huffman")


def main() -> None:
    """Ejecuta el ciclo principal del menú."""
    ruta_grafo = "data/grafos/grafo_ejemplo.csv"
    ruta_texto = "data/textos/texto_huffman.txt"

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "0":
            print("Saliendo del programa...")
            break
        elif opcion == "1":
            ejecutar_prim(ruta_grafo)
        elif opcion == "2":
            ejecutar_kruskal(ruta_grafo)
        elif opcion == "3":
            origen = input("Ingresa el nodo origen para Dijkstra (ej. A): ").strip()
            ejecutar_dijkstra(ruta_grafo, origen)
        elif opcion == "4":
            ejecutar_huffman(ruta_texto)
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()
