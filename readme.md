# Proyecto Final – Implementación y Visualización de Algoritmos Avanzados  
### Curso: Análisis de Algoritmos  
### Universidad Da Vinci de Guatemala 
**Estudiante:** Ashley Dayane Alfaro Aguilar  
**Carné:** 202301982  
**Fecha:** 1 de diciembre del 2025 



## 1. Objetivo general

Desarrollar un proyecto integral en Python que implemente, analice y visualice los algoritmos **Prim**, **Kruskal**, **Dijkstra** y **Huffman**, leyendo datos desde archivos externos, generando salidas gráficas en formato PNG y aplicando un flujo de trabajo profesional basado en **Gitflow**.



## 2. Objetivos específicos

- Implementar de forma modular los algoritmos:
  - Prim (Árbol de Expansión Mínima – MST).
  - Kruskal (Árbol de Expansión Mínima – MST).
  - Dijkstra (rutas más cortas en grafos ponderados).
  - Huffman (codificación óptima sin pérdida).
- Leer **grafos** desde archivos CSV y **textos** desde archivos `.txt`.
- Generar imágenes **PNG** como evidencia visual del procesamiento de cada algoritmo.
- Documentar el proyecto de forma clara y profesional mediante este `README.md`.
- Aplicar **Gitflow** utilizando ramas `main`, `develop`, `feature/*`, `release` y `hotfix`, así como PRs, merges y tags.
- Explicar la **complejidad teórica** (O grande) de cada algoritmo implementado.



## 3. Descripción general del proyecto

El proyecto consiste en un programa en Python que permite ejecutar desde un menú los algoritmos **Prim**, **Kruskal**, **Dijkstra** y **Huffman**.  
Los grafos son **no dirigidos y ponderados**, leídos desde un archivo CSV, y el texto para Huffman se lee desde un archivo **.txt**.

Cada ejecución:

- Muestra resultados en consola (aristas del MST, distancias mínimas, caminos, tabla de códigos).
- Genera una imagen PNG con el resultado gráfico.
- Permite evidenciar el funcionamiento de los algoritmos para la evaluación del curso.



## 4. Teoría de los algoritmos implementados

### Prim – Árbol de Expansión Mínima (MST)

El algoritmo de **Prim** construye un Árbol de Expansión Mínima partiendo de un vértice inicial y, en cada paso, agrega la arista de menor peso que conecta el árbol actual con algún vértice aún no visitado.  
Se utiliza típicamente una **cola de prioridad (heap)** para seleccionar la arista mínima de forma eficiente.



### Kruskal – Árbol de Expansión Mínima (MST)

El algoritmo de **Kruskal** ordena todas las aristas del grafo por peso creciente y las va agregando al MST siempre que no formen ciclos.  
Para detectar ciclos se utiliza una estructura **Union-Find** (Disjoint Set Union).


### Dijkstra – Caminos más cortos

El algoritmo de **Dijkstra** calcula las distancias mínimas desde un vértice origen en un grafo con pesos no negativos usando una cola de prioridad.


### Huffman – Codificación óptima

La **codificación de Huffman** asigna códigos más cortos a símbolos más frecuentes y códigos más largos a símbolos menos frecuentes, generando compresión sin pérdida.


## 5. Complejidad teórica (O grande)

- **Prim:** O(E log V)
- **Kruskal:** O(E log V)
- **Dijkstra:** O(E log V)
- **Huffman:** O(n log k)


## 6. Formatos de entrada

### Grafo (CSV)

```csv
origen,destino,peso
A,B,4
A,C,2
B,C,5
B,D,10
C,D,3
D,E,7
```
### Texto (Huffman)
```
En este archivo de texto se incluyen espacios, comas, puntos, letras mayúsculas y minúsculas, para que el árbol generado sea más complejo.
El objetivo es que las y los estudiantes analicen las frecuencias de cada carácter y construyan una tabla de códigos binarios eficiente.
Adicional agregamos caracteres especiales 		//..'';;;';.!@#$%^&*()^#$@!$@%^&*^()$#@!~%$@^&*(()_(*&^%#$@!«»»«»«×«»'
```
## 7. Estructura del proyecto 

![](/docs/evidencias/estructura.png)

## 8. Ejecución del programa 

![](/docs/evidencias/Ejecucion.png)

- **Prim**
![](/docs/evidencias/prim_mst_vista.png)
- **Kruskal**
![](/docs/evidencias/kruskal_mst_vista.png)
- **Dijkstra**
![](/docs/evidencias/dijkstra_paths_vista.png)
- **Huffman**
![](/docs/evidencias/huffman.png)

## 9. Imágenes Generadas 

- **prim_mst.png**
![](/docs/evidencias/prim_mst.png)
- **kruskal_mst.png**
![](/docs/evidencias/kruskal_mst.png)
- **dijkstra_paths.png**
![](/docs/evidencias/dijkstra_paths.png)
- **huffman_freq.png**
![](/docs/evidencias/huffman_freq.png)
- **huffman_tree.png**
![](/docs/evidencias/huffman_tree.png)


## 10. Git Flow aplicado 

- **main**
- **develop**
- **feature/prim**
- **feature/kruskal**
- **feature/dijkstra**
- **feature/huffman**
- **release/v1.0.0**
- **hotfix/readme**
- **Tag v1.0.0**

Incluye PRs: 
- **feature/prim → develop**
- **develop → main**

## 11. Conclusiones 
- Se implementaron correctamente 4 algoritmos fundamentales.
- Se aplicó Gitflow profesional.
- Se generaron salidas visuales claras.
- Se mantuvo un código modular, documentado y mantenible.

