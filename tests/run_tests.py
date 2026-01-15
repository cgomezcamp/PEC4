#!/usr/bin/env python3
"""
Script para ejecutar todos los tests unitarios del proyecto PEC4
"""

import unittest
import sys
import os

# Agregar el directorio actual al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def run_all_tests():
    """Ejecuta todos los tests unitarios"""

    # Crear un test loader
    loader = unittest.TestLoader()

    # Crear una suite de tests
    suite = unittest.TestSuite()

    # Cargar todos los tests de cada módulo
    test_modules = [
        'test_ejercicio1',
        'test_ejercicio2',
        'test_ejercicio3',
        'test_ejercicio4',
        'test_ejecutar_ejercicios',
        'test_main'
    ]

    print("="*70)
    print("EJECUTANDO TESTS UNITARIOS - PEC4")
    print("="*70)
    print()

    for module in test_modules:
        try:
            tests = loader.loadTestsFromName(module)
            suite.addTests(tests)
            print(f"✓ Tests cargados de: {module}")
        except Exception as e:
            print(f"✗ Error cargando {module}: {e}")

    print()
    print("="*70)
    print("EJECUTANDO TESTS")
    print("="*70)
    print()

    # Ejecutar los tests con verbosidad
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print()
    print("="*70)
    print("RESUMEN DE RESULTADOS")
    print("="*70)
    print(f"Tests ejecutados: {result.testsRun}")
    print(f"Exitosos: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Fallos: {len(result.failures)}")
    print(f"Errores: {len(result.errors)}")
    print("="*70)

    # Retornar código de salida apropiado
    return 0 if result.wasSuccessful() else 1


def run_specific_test(test_name):
    """
    Ejecuta un test específico

    Parameters
    ----------
    test_name : str
        Nombre del módulo de test (sin .py)
    """
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromName(test_name)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    if len(sys.argv) > 1:
        # Si se proporciona un argumento, ejecutar solo ese test
        test_name = sys.argv[1]
        print(f"Ejecutando solo: {test_name}")
        sys.exit(run_specific_test(test_name))
    else:
        # Sin argumentos, ejecutar todos los tests
        sys.exit(run_all_tests())
