"""
Ejercicio 1: Load dataset y EDA (Exploratory Data Analysis).

Este módulo contiene funciones para cargar datasets y realizar
análisis exploratorio de datos.
"""

import pandas as pd
from pathlib import Path


def load_dataset(path: str | None = None) -> pd.DataFrame:
    """
    Carga un dataset desde una ruta proporcionada o pregunta al usuario.

    Parameters
    ----------
    path : str | None
        Ruta al archivo del dataset. Si es None, pregunta opciones.

    Returns
    -------
    pd.DataFrame
        DataFrame cargado.
    """
    # Si NO se proporciona path, preguntar por las opciones
    if path is None:
        datasets = {
            "1": Path("data/rendiment_estudiants.xlsx"),
            "2": Path("data/taxa_abandonament.xlsx")
        }

        print("Opciones disponibles:")
        print("  1 - rendiment_estudiants.xlsx")
        print("  2 - taxa_abandonament.xlsx")

        choice = input("Selecciona una opción (1/2): ").strip()

        if choice not in datasets:
            raise ValueError("Opción no válida. Debe ser 1 o 2.")

        path = str(datasets[choice])

    # Cargar el dataset
    print(f"   Cargando desde: {path}")
    df = pd.read_excel(path)
    print(f"   ✓ {df.shape[0]} filas, {df.shape[1]} columnas")

    return df


def mostrar_primeras_filas(df: pd.DataFrame, n: int = 5) -> None:
    """
    Muestra las primeras n filas del DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame a mostrar.
    n : int, optional
        Número de filas a mostrar (default: 5).
    """
    print(f"\n{'='*60}")
    print(f"1.1. PRIMERAS {n} FILAS DEL DATASET")
    print("="*60)
    print(df.head(n))


def mostrar_columnas(df: pd.DataFrame) -> None:
    """
    Muestra las columnas del DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame del que mostrar las columnas.
    """
    print(f"\n{'='*60}")
    print("1.2. COLUMNAS DEL DATASET")
    print("="*60)
    print(f"Total de columnas: {len(df.columns)}\n")
    for i, col in enumerate(df.columns, 1):
        print(f"  {i}. {col}")


def mostrar_info(df: pd.DataFrame) -> None:
    """
    Muestra información del DataFrame (info()).

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame del que mostrar la información.
    """
    print(f"\n{'='*60}")
    print("1.3. INFORMACIÓN DEL DATASET")
    print("="*60)
    print(df.info())


def realizar_eda(df: pd.DataFrame) -> None:
    """
    Realiza análisis exploratorio de datos completo.

    Ejecuta todas las funciones de exploración:
    - Muestra primeras 5 filas
    - Muestra columnas
    - Muestra información del DataFrame

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame a analizar.
    """
    mostrar_primeras_filas(df)
    mostrar_columnas(df)
    mostrar_info(df)
