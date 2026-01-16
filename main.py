"""
Main: Punto de entrada principal del proyecto PEC4.

Ejecuta los ejercicios de la PEC4 de forma modular.
"""

import argparse
import sys
import traceback

from src.utils.ejecutar_ejercicios import ejecutar_ejercicio1, ejecutar_ejercicio2, ejecutar_ejercicio3, ejecutar_ejercicio4


def main():
    """Función principal."""
    parser = argparse.ArgumentParser(
        description='PEC4: Análisis de Rendimiento y Abandono Universitario',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python main.py              Ejecuta todos los ejercicios
  python main.py -ex 1        Ejecuta solo el ejercicio 1 (EDA)
  python main.py -ex 2        Ejecuta solo el ejercicio 2 (Limpieza y fusión)
  python main.py -ex 3        Ejecuta solo el ejercicio 3 (Análisis visual)
  python main.py -ex 4        Ejecuta solo el ejercicio 4 (Estadística avanzada)
  python main.py --help       Muestra esta ayuda

Comandos de tests:
  # Ejecutar todos los tests
  $env:PYTHONPATH = $PWD
  python tests/run_tests.py

  # Ejecutar test específico
  python -m unittest tests.test_ejercicio1 -v

  # Cobertura de código
  coverage run -m unittest discover -s tests -p "test_*.py"
  coverage report -m
  coverage html

Comandos de documentación:
  # Generar documentación HTML con Sphinx
  cd docs
  sphinx-build -b html source build/html
  start build/html/index.html

Comandos de linter:
  # Análisis con pylint
  pylint src/ main.py

  # Reporte detallado con score
  pylint src/ main.py --reports=y

Más información:
  Consulta el README.md para información detallada sobre:
  - Estructura del proyecto
  - Instalación y configuración del entorno virtual
  - Descripción de cada ejercicio
  - Gestión de dependencias
        """
    )

    parser.add_argument(
        '-ex',
        type=int,
        choices=[1, 2, 3, 4],
        metavar='N',
        help='Ejecuta solo el ejercicio N (disponibles: 1, 2, 3, 4)'
    )

    args = parser.parse_args()

    # Banner
    print("\n" + "█"*60)
    print("█" + " "*58 + "█")
    print("█" + "  PEC4: ANÁLISIS DE DATOS UNIVERSITARIOS  ".center(58) +
          "█")
    print("█" + " "*58 + "█")
    print("█"*60)

    try:
        # Determinar qué ejecutar
        if args.ex == 1:
            ejecutar_ejercicio1()
        elif args.ex == 2:
            ejecutar_ejercicio2()
        elif args.ex == 3:
            ejecutar_ejercicio3()
        elif args.ex == 4:
            ejecutar_ejercicio4()
        else:
            # Si no se especifica ejercicio, ejecutar todos en orden
            ejecutar_ejercicio1()
            ejecutar_ejercicio2()
            ejecutar_ejercicio3()
            ejecutar_ejercicio4()

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
