"""
Ejercicio 2: Limpieza de datos y fusión de datasets.

Este módulo contiene funciones para limpiar, homogeneizar y fusionar
los datasets de rendimiento y abandono.
"""

import os
import pandas as pd


def renombrar_columnas_abandono(df_abandono: pd.DataFrame) -> pd.DataFrame:
    """
    Renombra las columnas del dataset de abandono para que coincidan
    con las del dataset de rendimiento.

    Parameters
    ----------
    df_abandono : pd.DataFrame
        DataFrame de abandono con columnas originales.

    Returns
    -------
    pd.DataFrame
        DataFrame con columnas renombradas.
    """
    print("2.1. Renombrando columnas del dataset de abandono...")

    # Mapeo de nombres de columnas
    renombrado = {
        'Naturalesa universitat responsable': 'Tipus universitat',
        'Universitat Responsable': 'Universitat',
        'Sexe Alumne': 'Sexe',
        'Tipus de centre': 'Integrat S/N'
    }

    df_renombrado = df_abandono.rename(columns=renombrado)
    print(f"   ✓ {len(renombrado)} columnas renombradas")

    return df_renombrado


def eliminar_columnas(df_rendimiento: pd.DataFrame,
                      df_abandono: pd.DataFrame) -> tuple:
    """
    Elimina columnas innecesarias de ambos DataFrames.

    Elimina de ambos: 'Universitat', 'Unitat'
    Elimina de rendimiento: 'Crèdits ordinaris superats',
                           'Crèdits ordinaris matriculats'

    Parameters
    ----------
    df_rendimiento : pd.DataFrame
        DataFrame de rendimiento.
    df_abandono : pd.DataFrame
        DataFrame de abandono.

    Returns
    -------
    tuple
        (df_rendimiento_limpio, df_abandono_limpio)
    """
    print("\n2.2. Eliminando columnas innecesarias...")

    # Columnas a eliminar de ambos datasets
    columnas_comunes = ['Universitat', 'Unitat']

    # Columnas adicionales a eliminar de rendimiento
    columnas_rendimiento = columnas_comunes + [
        'Crèdits ordinaris superats',
        'Crèdits ordinaris matriculats'
    ]

    # Eliminar columnas que existan
    df_rend_limpio = df_rendimiento.drop(
        columns=[col for col in columnas_rendimiento
                 if col in df_rendimiento.columns]
    )

    df_aban_limpio = df_abandono.drop(
        columns=[col for col in columnas_comunes
                 if col in df_abandono.columns]
    )

    print(f"   ✓ Rendimiento: {df_rendimiento.shape[1]} → "
          f"{df_rend_limpio.shape[1]} columnas")
    print(f"   ✓ Abandono: {df_abandono.shape[1]} → "
          f"{df_aban_limpio.shape[1]} columnas")

    return df_rend_limpio, df_aban_limpio


def agrupar_por_caracteristicas(df: pd.DataFrame,
                                columna_valor: str) -> pd.DataFrame:
    """
    Agrupa el DataFrame por características comunes y calcula la media.

    Agrupa por: ['Curs Acadèmic', 'Tipus universitat', 'Sigles',
                 'Tipus Estudi', 'Branca', 'Sexe', 'Integrat S/N']

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame a agrupar.
    columna_valor : str
        Nombre de la columna con los valores a promediar
        ('Taxa rendiment' o '% Abandonament a primer curs').

    Returns
    -------
    pd.DataFrame
        DataFrame agrupado con la media de la columna especificada.
    """
    print("\n2.3. Agrupando datos por características comunes...")

    # Columnas por las que agrupar
    columnas_agrupacion = [
        'Curs Acadèmic',
        'Tipus universitat',
        'Sigles',
        'Tipus Estudi',
        'Branca',
        'Sexe',
        'Integrat S/N'
    ]

    # Filtrar solo las columnas que existen en el DataFrame
    columnas_existentes = [col for col in columnas_agrupacion
                           if col in df.columns]

    print(f"   Agrupando por: {columnas_existentes}")
    print(f"   Calculando media de: {columna_valor}")

    # Agrupar y calcular media
    df_agrupado = df.groupby(columnas_existentes, as_index=False).agg({
        columna_valor: 'mean'
    })

    print(f"   ✓ {df.shape[0]} → {df_agrupado.shape[0]} filas")

    return df_agrupado


def fusionar_datasets(df_rendimiento: pd.DataFrame,
                      df_abandono: pd.DataFrame) -> pd.DataFrame:
    """
    Fusiona los datasets de rendimiento y abandono.

    Realiza un merge interno (inner join) para mantener solo las filas
    que coinciden en ambos datasets.

    Parameters
    ----------
    df_rendimiento : pd.DataFrame
        DataFrame de rendimiento agrupado.
    df_abandono : pd.DataFrame
        DataFrame de abandono agrupado.

    Returns
    -------
    pd.DataFrame
        DataFrame fusionado.
    """
    print("\n2.4. Fusionando datasets...")

    # Identificar columnas comunes (excluyendo las de valores)
    columnas_rendimiento = set(df_rendimiento.columns)
    columnas_abandono = set(df_abandono.columns)

    # Columnas comunes excluyendo las métricas
    columnas_merge = list(
        (columnas_rendimiento & columnas_abandono) -
        {'Taxa rendiment', '% Abandonament a primer curs'}
    )

    print(f"   Fusionando por: {columnas_merge}")

    # Fusionar con inner join
    df_fusionado = pd.merge(
        df_rendimiento,
        df_abandono,
        on=columnas_merge,
        how='inner'
    )

    print(f"   ✓ Dataset fusionado: {df_fusionado.shape[0]} filas, "
          f"{df_fusionado.shape[1]} columnas")

    return df_fusionado


def limpiar_y_fusionar(df_rendimiento: pd.DataFrame,
                       df_abandono: pd.DataFrame) -> pd.DataFrame:
    """
    Ejecuta todo el proceso de limpieza y fusión.

    Pasos:
    1. Renombrar columnas de abandono
    2. Eliminar columnas innecesarias
    3. Agrupar ambos datasets por características
    4. Fusionar datasets

    Parameters
    ----------
    df_rendimiento : pd.DataFrame
        DataFrame de rendimiento original.
    df_abandono : pd.DataFrame
        DataFrame de abandono original.

    Returns
    -------
    pd.DataFrame
        DataFrame fusionado y limpio.
    """
    print("\n" + "="*60)
    print("EJERCICIO 2: LIMPIEZA Y FUSIÓN DE DATOS")
    print("="*60)

    # Paso 2.1: Renombrar columnas
    df_abandono_renombrado = renombrar_columnas_abandono(df_abandono)

    # Paso 2.2: Eliminar columnas innecesarias
    df_rend_limpio, df_aban_limpio = eliminar_columnas(
        df_rendimiento,
        df_abandono_renombrado
    )

    # Paso 2.3: Agrupar por características
    df_rend_agrupado = agrupar_por_caracteristicas(
        df_rend_limpio,
        'Taxa rendiment'
    )

    df_aban_agrupado = agrupar_por_caracteristicas(
        df_aban_limpio,
        '% Abandonament a primer curs'
    )

    # Paso 2.4: Fusionar
    df_fusionado = fusionar_datasets(df_rend_agrupado, df_aban_agrupado)

    # Guardar dataset
    # 1. Crear la carpeta 'data' si no existe para evitar errores
    if not os.path.exists('data'):
        os.makedirs('data')
        print("\n📁 Carpeta 'data' creada.")

    # 2. Definir la ruta y guardar
    ruta_archivo = 'data/dataset_fusionado.csv'
    df_fusionado.to_csv(ruta_archivo, index=False, encoding='utf-8')

    print(f"\n💾 Dataset guardado exitosamente en: {ruta_archivo}")

    print("\n✅ Proceso de limpieza y fusión completado")

    return df_fusionado
