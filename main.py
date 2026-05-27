# main.py

from data import peliculas

from engine import (
    filtrar_peliculas_validas,
    filtrar_por_genero,
    filtrar_peliculas_recientes,
    puntuar_peliculas,
    ordenar_top_peliculas,
    calcular_puntaje_total,
    calcular_promedio_rating,
    contar_total_likes,
    combinar_nombres_y_puntajes,
    convertir_a_resumen,
    generar_recomendaciones
)


def mostrar_titulo():
    print("=" * 50)
    print("      NETFLIX BIG DATA FUNCIONAL")
    print("=" * 50)


def mostrar_catalogo(catalogo):
    print("\nCATÁLOGO GENERAL:\n")

    for pelicula in catalogo:
        print(
            f"{pelicula['nombre']} | "
            f"{pelicula['genero']} | "
            f"Rating: {pelicula['rating']}"
        )


def ejecutar_pipeline_principal():
    print("\nPIPELINE FUNCIONAL\n")

    # =====================================================
    # FILTER
    # =====================================================

    peliculas_filtradas = filtrar_peliculas_validas(
        peliculas
    )

    print("1. FILTER -> Películas válidas:\n")

    for pelicula in peliculas_filtradas:
        print(
            f"- {pelicula['nombre']} "
            f"| Rating: {pelicula['rating']}"
        )

    # =====================================================
    # MAP
    # =====================================================

    peliculas_puntuadas = puntuar_peliculas(
        peliculas_filtradas
    )

    print("\n2. MAP -> Películas puntuadas:\n")

    for pelicula in peliculas_puntuadas:
        print(
            f"- {pelicula['nombre']} "
            f"| Puntaje: {pelicula['puntaje']}"
        )

    # =====================================================
    # SORTED
    # =====================================================

    top_peliculas = ordenar_top_peliculas(
        peliculas_puntuadas
    )

    print("\n3. SORTED -> Top recomendaciones:\n")

    for pelicula in top_peliculas:
        print(
            f"- {pelicula['nombre']} "
            f"| Puntaje: {pelicula['puntaje']}"
        )

    # =====================================================
    # REDUCE
    # =====================================================

    puntaje_total = calcular_puntaje_total(
        top_peliculas
    )

    promedio = calcular_promedio_rating(
        peliculas_filtradas
    )

    likes_totales = contar_total_likes(
        peliculas_filtradas
    )

    print("\n4. REDUCE -> Estadísticas:\n")

    print("Puntaje total:", puntaje_total)
    print("Promedio rating:", promedio)
    print("Likes totales:", likes_totales)

    # =====================================================
    # ZIP
    # =====================================================

    combinados = combinar_nombres_y_puntajes(
        top_peliculas
    )

    print("\n5. ZIP -> Datos combinados:\n")

    for dato in combinados:
        print(dato)


def ejecutar_consultas_extra():
    print("\nCONSULTAS ADICIONALES\n")

    # =====================================================
    # FILTRAR POR GÉNERO
    # =====================================================

    accion = filtrar_por_genero(
        peliculas,
        "Acción"
    )

    print("Películas de Acción:\n")

    for pelicula in accion:
        print("-", pelicula["nombre"])

    # =====================================================
    # PELÍCULAS RECIENTES
    # =====================================================

    recientes = filtrar_peliculas_recientes(
        peliculas,
        2018
    )

    print("\nPelículas recientes:\n")

    for pelicula in recientes:
        print(
            f"- {pelicula['nombre']} "
            f"({pelicula['anio']})"
        )


def ejecutar_resumenes():
    print("\nRESÚMENES GENERADOS CON MAP\n")

    resumenes = convertir_a_resumen(
        peliculas
    )

    for resumen in resumenes:
        print("-", resumen)


def ejecutar_recomendador_final():
    print("\nTOP 5 RECOMENDACIONES FINALES\n")

    recomendaciones = generar_recomendaciones(
        peliculas
    )

    for i, pelicula in enumerate(
        recomendaciones,
        start=1
    ):
        print(
            f"{i}. {pelicula['nombre']} "
            f"| Puntaje: {pelicula['puntaje']}"
        )


def finalizar():
    print("\n" + "=" * 50)
    print("        SISTEMA FINALIZADO")
    print("=" * 50)


def ejecutar_sistema():

    mostrar_titulo()

    mostrar_catalogo(peliculas)

    ejecutar_pipeline_principal()

    ejecutar_consultas_extra()

    ejecutar_resumenes()

    ejecutar_recomendador_final()

    finalizar()


if __name__ == "__main__":
    ejecutar_sistema()