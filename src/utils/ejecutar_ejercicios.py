import os
from pathlib import Path
import sys

import pandas as pd

from src.modules import ejercicio1, ejercicio2, ejercicio3, ejercicio4


def ejecutar_ejercicio1():
    """
    Ejecuta el Ejercicio 1: Load dataset y EDA.

    Parameters
    ----------
    ruta_dataset : str, optional
        Ruta al archivo del dataset. Si es None, pregunta al usuario.

    Returns
    -------
    pd.DataFrame
        DataFrame cargado.
    """
    print("\n" + "*"*60)
    print("EJERCICIO 1: LOAD DATASET Y EDA")
    print("*"*60)
    # Preguntar si quiere usar ruta personalizada
    print("\n" + "="*60)
    print("CONFIGURACIÓN INICIAL")
    print("="*60)

    usar_ruta_personalizada = input(
        "¿Deseas usar una ruta personalizada? (s/n): "
    ).strip().lower()

    ruta_dataset = None

    if usar_ruta_personalizada in ['s', 'si', 'sí', 'y', 'yes']:
        ruta_dataset = input(
            "Introduce la ruta del archivo: "
        ).strip()

        # Validar que existe
        if not Path(ruta_dataset).exists():
            print(f"\n❌ Error: No se encontró {ruta_dataset}")
            sys.exit(1)

        print("✓ Ruta configurada correctamente")

    # Cargar dataset
    print("\n📂 Cargando dataset...")
    df = ejercicio1.load_dataset(ruta_dataset)

    # Realizar EDA
    print("\n" + "="*60)
    print("ANÁLISIS EXPLORATORIO DE DATOS (EDA)")
    print("="*60)
    ejercicio1.realizar_eda(df)

    print("\n✅ Ejercicio 1 completado")

    return df


def ejecutar_ejercicio2():
    """
    Ejecuta el Ejercicio 2: Limpieza y fusión de datos.
    Carga los datos Excel, ejecuta la función de limpieza y fusión.

    Returns
    -------
    pd.DataFrame
        DataFrame fusionado.
    """

    # Definir rutas de los archivos
    ruta_rendimiento = 'data/rendiment_estudiants.xlsx'
    ruta_abandono = 'data/taxa_abandonament.xlsx'

    df_rendimiento = pd.read_excel(ruta_rendimiento)
    df_abandono = pd.read_excel(ruta_abandono)

    # Ejecutar limpieza y fusión
    df_fusionado = ejercicio2.limpiar_y_fusionar(
        df_rendimiento,
        df_abandono
    )

    # Mostrar muestra del resultado
    print("\n" + "="*60)
    print("MUESTRA DEL DATASET FUSIONADO")
    print("="*60)
    print(df_fusionado.head(10))

    print("\n✅ Ejercicio 2 completado")

    return df_fusionado


def ejecutar_ejercicio3():
    """
    Ejecuta el Ejercicio 3: Análisis Visual.
    """
    print("\n" + "*"*60)
    print("EJERCICIO 3: ANÁLISIS VISUAL DE TENDENCIAS")
    print("*"*60)

    ruta_fusionado = 'data/dataset_fusionado.csv'

    if not os.path.exists(ruta_fusionado):
        print(f"⚠️ El archivo {ruta_fusionado} no existe. Ejecutando Ejer 2")
        df_fusionado = ejecutar_ejercicio2()
    else:
        print(f"📂 Cargando dataset fusionado desde {ruta_fusionado}...")
        df_fusionado = pd.read_csv(ruta_fusionado)

    # Solicitar nombre para el archivo
    nombre = input("Introduce tu nombre para el archivo de salida: ").strip()
    if not nombre:
        nombre = "alumno"

    ejercicio3.generar_graficos_series_temporales(df_fusionado, nombre)

    print("\n✅ Ejercicio 3 completado")


def ejecutar_ejercicio4():
    """
    Ejecuta el Ejercicio 4: Análisis Estadístico.
    """
    print("\n" + "*"*60)
    print("EJERCICIO 4: ANÁLISIS ESTADÍSTICO AUTOMATIZADO")
    print("*"*60)

    ruta_fusionado = 'data/dataset_fusionado.csv'

    if not os.path.exists(ruta_fusionado):
        print("⚠️ El dataset fusionado no existe. Ejecutando Ejer 2")
        df_fusionado = ejecutar_ejercicio2()
    else:
        df_fusionado = pd.read_csv(ruta_fusionado)

    # Llamar al análisis
    ejercicio4.analyze_dataset(df_fusionado)

    print("\n✅ Ejercicio 4 completado")
