# engine.py

from functools import reduce


# =========================================================
# FILTERS
# =========================================================

def filtrar_peliculas_validas(catalogo):
    """
    Filtra películas:
    - rating >= 8
    - no vistas
    - disponibles en Perú
    """
    return list(filter(
        lambda p: (
            p["rating"] >= 8 and
            not p["vistas"] and
            p["region"] == "Perú"
        ),
        catalogo
    ))


def filtrar_por_genero(catalogo, genero):
    """Filtra películas por género."""
    return list(filter(
        lambda p: p["genero"] == genero,
        catalogo
    ))


def filtrar_por_plataforma(catalogo, plataforma):
    """Filtra películas por plataforma."""
    return list(filter(
        lambda p: p["plataforma"] == plataforma,
        catalogo
    ))


def filtrar_peliculas_recientes(catalogo, anio_minimo):
    """Filtra películas recientes."""
    return list(filter(
        lambda p: p["anio"] >= anio_minimo,
        catalogo
    ))


# =========================================================
# MAP
# =========================================================

def puntuar_peliculas(catalogo_filtrado):
    """
    Calcula puntuación personalizada.
    Fórmula:
    rating * likes / 1000
    """
    return list(map(
        lambda p: {
            "nombre": p["nombre"],
            "genero": p["genero"],
            "plataforma": p["plataforma"],
            "puntaje": round(
                (p["rating"] * p["likes"]) / 1000,
                2
            )
        },
        catalogo_filtrado
    ))


def obtener_nombres(catalogo):
    """Obtiene solo los nombres."""
    return list(map(
        lambda p: p["nombre"],
        catalogo
    ))


def convertir_a_resumen(catalogo):
    """Crea resúmenes simplificados."""
    return list(map(
        lambda p: (
            f"{p['nombre']} "
            f"({p['genero']}) "
            f"- Rating: {p['rating']}"
        ),
        catalogo
    ))


# =========================================================
# SORT
# =========================================================

def ordenar_top_peliculas(catalogo_puntuado):
    """Ordena por puntaje descendente."""
    return sorted(
        catalogo_puntuado,
        key=lambda p: p["puntaje"],
        reverse=True
    )


def ordenar_por_rating(catalogo):
    """Ordena películas por rating."""
    return sorted(
        catalogo,
        key=lambda p: p["rating"],
        reverse=True
    )


# =========================================================
# REDUCE
# =========================================================

def calcular_puntaje_total(top_peliculas):
    """Suma total de puntajes."""
    return reduce(
        lambda acumulador, pelicula:
            acumulador + pelicula["puntaje"],
        top_peliculas,
        0
    )


def calcular_promedio_rating(catalogo):
    """Calcula promedio de ratings."""
    if len(catalogo) == 0:
        return 0

    suma = reduce(
        lambda acc, p: acc + p["rating"],
        catalogo,
        0
    )

    return round(suma / len(catalogo), 2)


def contar_total_likes(catalogo):
    """Cuenta likes totales."""
    return reduce(
        lambda acc, p: acc + p["likes"],
        catalogo,
        0
    )


# =========================================================
# ZIP
# =========================================================

def combinar_nombres_y_puntajes(top_peliculas):
    """Combina nombres y puntajes."""
    nombres = list(map(
        lambda p: p["nombre"],
        top_peliculas
    ))

    puntajes = list(map(
        lambda p: p["puntaje"],
        top_peliculas
    ))

    return list(zip(nombres, puntajes))


# =========================================================
# PIPELINE FUNCIONAL
# =========================================================

def generar_recomendaciones(catalogo):
    """
    Pipeline completo:
    filter -> map -> sort
    """

    peliculas_validas = filtrar_peliculas_validas(catalogo)

    peliculas_puntuadas = puntuar_peliculas(
        peliculas_validas
    )

    top = ordenar_top_peliculas(
        peliculas_puntuadas
    )

    return top[:5]