# Practicas_IA_ESCOM
# Prácticas de Inteligencia Artificial - ESCOM

Este repositorio contiene las prácticas desarrolladas en el curso de **Inteligencia Artificial**, y estan organizadas por parciales.

Los programas implementan algoritmos clásicos de búsqueda, agentes, lógica y regresión, utilizando únicamente **librerías nativas de Python**, anexando:

- `numpy` → manejo de arreglos.
- `matplotlib` → graficación y visualización de resultados.
- `timeit` → medición de tiempos de ejecución.
- `random` → generación de aleatoriedad en pruebas.
- `tracemalloc` → análisis de memoria.

Todo lo demás está construido **con lo nativo de Python** (estructuras, algoritmos y funciones propias).

---

## 📂 Contenido

### 🔹 1er Parcial
- `append_no_librerias.py` → manejo básico de listas y estructuras sin librerías externas.
- `comparacion_memoria_tiempo_agentes.py` → comparación de consumo de memoria y tiempo en agentes dfs y bfs.
- `grafos_bfs_dfs.py` → implementación de búsqueda en grafos con BFS y DFS.

### 🔹 2do Parcial
- **Laberintos con agentes y algoritmos de búsqueda**:
  - `laberinto_bfs_grafico.py`  
  - `laberinto_dfs_grafico.py`
  - `laberinto_dijkstra_grafico.py`
  - `laberinto_a_estrella_grafico.py`
- `Union_metodos_laberinto/` → integración de todos los algoritmos en un solo programa con comparativa gráfica de tiempos.

### 🔹 3er Parcial
- **Agentes**:
  - `carrera_2_agentes_reynas_no_atacan.py` → Laberinto con agentes dfs y bfs, que compiten por recorrer reynas del laberinto.
  - `carrera_agentes_modificados.py` → Agentes básicos con modificaciones de reglas de movimiento
  - `carrera_bfs_dfs_grafico.py`
- **Lógica y razonamiento**:  
  - `logica_1er_orden.py` → resuelve árbol genealógico a través de una base de conocimiento
- **Regresión**:
  - `regresion_lineal.py` → Regresión lineal básica con gráfica visual
  - `regresion_ride.py` → Regresión de ride básica con gráfica visual 3D

---

## 🚀 Ejecución
Cada práctica puede ejecutarse directamente con **Python 3** o usando colab:

```bash
python nombre_del_archivo.py
