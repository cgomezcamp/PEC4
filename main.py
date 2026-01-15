"""
Main: Punto de entrada principal del proyecto PEC4.

Ejecuta los ejercicios de la PEC4 de forma modular.
"""

import argparse
import sys
import traceback
from pathlib import Path

from src.modules import ejercicio1


def ejecutar_ejercicio1(ruta_dataset=None):
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


def main():
    """Función principal."""
    parser = argparse.ArgumentParser(
        description='PEC4: Análisis de Rendimiento y Abandono Universitario',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python main.py              Ejecuta todos los ejercicios
  python main.py -ex 1        Ejecuta el ejercicio 1
  python main.py --help       Muestra esta ayuda
        """
    )

    parser.add_argument(
        '-ex',
        type=int,
        choices=[1],
        metavar='N',
        help='Ejecuta el ejercicio N (disponibles: 1)'
    )

    args = parser.parse_args()

    # Determinar qué ejercicios ejecutar
    if args.ex is None:
        ejercicios_a_ejecutar = 1
    else:
        ejercicios_a_ejecutar = args.ex

    # Banner
    print("\n" + "█"*60)
    print("█" + " "*58 + "█")
    print("█" + "  PEC4: ANÁLISIS DE DATOS UNIVERSITARIOS  ".center(58) +
          "█")
    print("█" + " "*58 + "█")
    print("█"*60)

    # Preguntar SOLO si quiere usar ruta personalizada
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

    try:
        # Ejecutar ejercicios
        if ejercicios_a_ejecutar >= 1:
            df = ejecutar_ejercicio1(ruta_dataset)

        # Resumen
        print("\n" + "="*60)
        print("RESUMEN DE EJECUCIÓN")
        print("="*60)
        print("✅ Ejercicio 1 completado exitosamente")
        print(f"   • Dataset: {df.shape[0]} registros, "
              f"{df.shape[1]} columnas")

        print("\n" + "█"*60)
        print("█" + " "*58 + "█")
        print("█" + "  ✅ EJECUCIÓN COMPLETADA  ".center(58) + "█")
        print("█" + " "*58 + "█")
        print("█"*60 + "\n")

    except FileNotFoundError as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
