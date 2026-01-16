"""
Tests unitarios para ejercicio1.py
"""

import unittest
from unittest.mock import patch
import pandas as pd
import sys
import os
from io import StringIO


# Importar el módulo a testear
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root_dir)
from src.modules import ejercicio1


class TestLoadDataset(unittest.TestCase):
    """Tests para la función load_dataset"""

    @patch('src.modules.ejercicio1.pd.read_excel')
    def test_load_dataset_con_path_valido(self, mock_read_excel):
        """Test carga de dataset con path válido proporcionado"""
        mock_df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        mock_read_excel.return_value = mock_df

        resultado = ejercicio1.load_dataset('data/test.xlsx')

        mock_read_excel.assert_called_once_with('data/test.xlsx')
        self.assertEqual(resultado.shape, (2, 2))
        pd.testing.assert_frame_equal(resultado, mock_df)

    @patch('src.modules.ejercicio1.pd.read_excel')
    @patch('builtins.input', return_value='1')
    def test_load_dataset_sin_path_opcion_1(self, mock_input, mock_read_excel):
        """Test carga de dataset sin path, seleccionando opción 1"""
        mock_df = pd.DataFrame({'col1': [1, 2, 3]})
        mock_read_excel.return_value = mock_df

        resultado = ejercicio1.load_dataset(None)

        mock_input.assert_called_once()
        # Verificar que se llamó con alguna ruta que contiene rendiment_estudiants.xlsx
        call_args = mock_read_excel.call_args[0][0]
        self.assertIn('rendiment_estudiants.xlsx', str(call_args))
        self.assertEqual(resultado.shape[0], 3)

    @patch('src.modules.ejercicio1.pd.read_excel')
    @patch('builtins.input', return_value='2')
    def test_load_dataset_sin_path_opcion_2(self, mock_input, mock_read_excel):
        """Test carga de dataset sin path, seleccionando opción 2"""
        mock_df = pd.DataFrame({'col1': [1, 2, 3, 4]})
        mock_read_excel.return_value = mock_df

        resultado = ejercicio1.load_dataset(None)

        # Verificar que se llamó con alguna ruta que contiene taxa_abandonament.xlsx
        call_args = mock_read_excel.call_args[0][0]
        self.assertIn('taxa_abandonament.xlsx', str(call_args))
        self.assertEqual(resultado.shape[0], 4)

    @patch('builtins.input', return_value='3')
    def test_load_dataset_opcion_invalida(self, mock_input):
        """Test que verifica error con opción inválida"""
        with self.assertRaises(ValueError) as context:
            ejercicio1.load_dataset(None)

        self.assertIn("no válida", str(context.exception))


class TestMostrarPrimerasFilas(unittest.TestCase):
    """Tests para la función mostrar_primeras_filas"""

    @patch('sys.stdout', new_callable=StringIO)
    def test_mostrar_primeras_filas_default(self, mock_stdout):
        """Test mostrar primeras 5 filas por defecto"""
        df = pd.DataFrame({'A': range(10), 'B': range(10, 20)})

        ejercicio1.mostrar_primeras_filas(df)

        output = mock_stdout.getvalue()
        self.assertIn('PRIMERAS 5 FILAS', output)
        self.assertIn('=', output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_mostrar_primeras_filas_custom(self, mock_stdout):
        """Test mostrar n filas personalizado"""
        df = pd.DataFrame({'A': range(10), 'B': range(10, 20)})

        ejercicio1.mostrar_primeras_filas(df, n=3)

        output = mock_stdout.getvalue()
        self.assertIn('PRIMERAS 3 FILAS', output)


class TestMostrarColumnas(unittest.TestCase):
    """Tests para la función mostrar_columnas"""

    @patch('sys.stdout', new_callable=StringIO)
    def test_mostrar_columnas_basico(self, mock_stdout):
        """Test mostrar columnas de un DataFrame"""
        df = pd.DataFrame({
            'Columna1': [1, 2],
            'Columna2': [3, 4],
            'Columna3': [5, 6]
        })

        ejercicio1.mostrar_columnas(df)

        output = mock_stdout.getvalue()
        self.assertIn('COLUMNAS DEL DATASET', output)
        self.assertIn('Total de columnas: 3', output)
        self.assertIn('Columna1', output)
        self.assertIn('Columna2', output)
        self.assertIn('Columna3', output)


class TestMostrarInfo(unittest.TestCase):
    """Tests para la función mostrar_info"""

    @patch('sys.stdout', new_callable=StringIO)
    def test_mostrar_info(self, mock_stdout):
        """Test mostrar información del DataFrame"""
        df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': ['x', 'y', 'z']
        })

        ejercicio1.mostrar_info(df)

        output = mock_stdout.getvalue()
        self.assertIn('INFORMACIÓN DEL DATASET', output)
        self.assertIn('=', output)


class TestRealizarEDA(unittest.TestCase):
    """Tests para la función realizar_eda"""

    @patch('src.modules.ejercicio1.mostrar_info')
    @patch('src.modules.ejercicio1.mostrar_columnas')
    @patch('src.modules.ejercicio1.mostrar_primeras_filas')
    def test_realizar_eda_llama_todas_funciones(self, mock_filas, mock_cols,
                                                mock_info):
        """Test que realizar_eda llama a todas las funciones de análisis"""
        df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})

        ejercicio1.realizar_eda(df)

        mock_filas.assert_called_once_with(df)
        mock_cols.assert_called_once_with(df)
        mock_info.assert_called_once_with(df)


if __name__ == '__main__':
    unittest.main()
