# Netflix Big Data - Paradigma Funcional

Este proyecto simula el procesamiento de grandes volúmenes de datos (Big Data) aplicado a un motor de recomendación de contenido multimedia en tiempo real, inspirándose en el modelo de Netflix.

Fue desarrollado como parte de la Primera Unidad del curso de **Lenguajes de Programación**.

## Descripción Técnica

El sistema ha sido implementado en Python, utilizando exclusivamente constructos del **paradigma de programación funcional** para evitar los bucles iterativos tradicionales (estado mutable). Las operaciones de procesamiento de datos se realizan mediante funciones de primer orden:

*   **`filter`**: Filtrado instantáneo de películas ya visualizadas o fuera de la región del usuario.
*   **`map` & `zip`**: Cálculo de la puntuación de relevancia cruzando el perfil del usuario con los atributos de cada película.
*   **`reduce`**: Agregación de los datos procesados para extraer el Top de mejores recomendaciones.

## Estructura del Proyecto

El código está modularizado aplicando el principio de separación de responsabilidades:

*   `data.py`: Contiene la base de datos simulada (catálogo de películas).
*   `engine.py`: Encapsula toda la lógica del motor utilizando funciones puras.
*   `main.py`: Archivo principal que orquesta la ejecución e imprime los resultados por consola.

## Cómo ejecutarlo

Para correr la simulación localmente, asegúrate de tener Python instalado y ejecuta el siguiente comando en la terminal:

```bash
python main.py
