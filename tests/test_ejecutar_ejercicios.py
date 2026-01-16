"""
Tests unitarios para ejecutar_ejercicios.py
"""

import unittest
from unittest.mock import patch
import pandas as pd
import sys
import os


# Importar el módulo a testear
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root_dir)
from src.utils import ejecutar_ejercicios


class TestEjecutarEjercicio1(unittest.TestCase):
    """Tests para la función ejecutar_ejercicio1"""

    @patch('src.utils.ejecutar_ejercicios.ejercicio1.realizar_eda')
    @patch('src.utils.ejecutar_ejercicios.ejercicio1.load_dataset')
    @patch('builtins.input', return_value='n')
    def test_ejecutar_sin_ruta_personalizada(self, mock_input, mock_load,
                                             mock_eda):
        """Test ejecución sin ruta personalizada"""
        mock_df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        mock_load.return_value = mock_df

        resultado = ejecutar_ejercicios.ejecutar_ejercicio1()

        mock_input.assert_called_once()
        mock_load.assert_called_once_with(None)
        mock_eda.assert_called_once_with(mock_df)
        pd.testing.assert_frame_equal(resultado, mock_df)

    @patch('src.utils.ejecutar_ejercicios.ejercicio1.realizar_eda')
    @patch('src.utils.ejecutar_ejercicios.ejercicio1.load_dataset')
    @patch('src.utils.ejecutar_ejercicios.Path')
    @patch('builtins.input')
    def test_ejecutar_con_ruta_personalizada_valida(self, mock_input,
                                                    mock_path,
                                                    mock_load, mock_eda):
        """Test ejecución con ruta personalizada válida"""
        mock_input.side_effect = ['s', 'data/test.xlsx']
        mock_path.return_value.exists.return_value = True

        mock_df = pd.DataFrame({'col1': [1, 2]})
        mock_load.return_value = mock_df

        resultado = ejecutar_ejercicios.ejecutar_ejercicio1()

        self.assertEqual(mock_input.call_count, 2)
        mock_load.assert_called_once_with('data/test.xlsx')
        mock_eda.assert_called_once()

    @patch('src.utils.ejecutar_ejercicios.sys.exit')
    @patch('src.utils.ejecutar_ejercicios.Path')
    @patch('builtins.input')
    def test_ejecutar_con_ruta_invalida(self, mock_input,
                                        mock_path, mock_exit):
        """Test que sale del programa si la ruta no existe"""
        mock_input.side_effect = ['s', 'ruta/inexistente.xlsx']
        mock_path.return_value.exists.return_value = False

        ejecutar_ejercicios.ejecutar_ejercicio1()

        mock_exit.assert_called_once_with(1)


class TestEjecutarEjercicio2(unittest.TestCase):
    """Tests para la función ejecutar_ejercicio2"""

    @patch('src.utils.ejecutar_ejercicios.ejercicio2.limpiar_y_fusionar')
    @patch('src.utils.ejecutar_ejercicios.pd.read_excel')
    def test_ejecutar_ejercicio2_correcto(self, mock_read_excel, mock_limpiar):
        """Test ejecución correcta del ejercicio 2"""
        mock_df_rend = pd.DataFrame({'col1': [1, 2]})
        mock_df_aban = pd.DataFrame({'col2': [3, 4]})
        mock_df_fusionado = pd.DataFrame({'col1': [1], 'col2': [3]})

        mock_read_excel.side_effect = [mock_df_rend, mock_df_aban]
        mock_limpiar.return_value = mock_df_fusionado

        resultado = ejecutar_ejercicios.ejecutar_ejercicio2()

        self.assertEqual(mock_read_excel.call_count, 2)
        mock_read_excel.assert_any_call('data/rendiment_estudiants.xlsx')
        mock_read_excel.assert_any_call('data/taxa_abandonament.xlsx')
        mock_limpiar.assert_called_once()
        pd.testing.assert_frame_equal(resultado, mock_df_fusionado)


class TestEjecutarEjercicio3(unittest.TestCase):
    """Tests para la función ejecutar_ejercicio3"""

    @patch('src.utils.ejecutar_ejercicios.ejercicio3.generar_graficos_series_temporales')
    @patch('src.utils.ejecutar_ejercicios.pd.read_csv')
    @patch('src.utils.ejecutar_ejercicios.os.path.exists', return_value=True)
    @patch('builtins.input', return_value='TestUser')
    def test_ejecutar_con_archivo_existente(self, mock_input, mock_exists,
                                            mock_read_csv, mock_generar):
        """Test cuando el archivo fusionado ya existe"""
        mock_df = pd.DataFrame({'col1': [1, 2]})
        mock_read_csv.return_value = mock_df

        ejecutar_ejercicios.ejecutar_ejercicio3()

        mock_exists.assert_called_once_with('data/dataset_fusionado.csv')
        mock_read_csv.assert_called_once_with('data/dataset_fusionado.csv')
        mock_generar.assert_called_once_with(mock_df, 'TestUser')

    @patch('src.utils.ejecutar_ejercicios.ejercicio3.generar_graficos_series_temporales')
    @patch('src.utils.ejecutar_ejercicios.ejecutar_ejercicio2')
    @patch('src.utils.ejecutar_ejercicios.os.path.exists', return_value=False)
    @patch('builtins.input', return_value='TestUser')
    def test_ejecutar_sin_archivo_ejecuta_ejercicio2(self, mock_input,
                                                     mock_exists,
                                                     mock_ejercicio2,
                                                     mock_generar):
        """Test que ejecuta ejercicio 2 si no existe el archivo"""
        mock_df = pd.DataFrame({'col1': [1, 2]})
        mock_ejercicio2.return_value = mock_df

        ejecutar_ejercicios.ejecutar_ejercicio3()

        mock_exists.assert_called_once()
        mock_ejercicio2.assert_called_once()
        mock_generar.assert_called_once_with(mock_df, 'TestUser')

    @patch('src.utils.ejecutar_ejercicios.ejercicio3.generar_graficos_series_temporales')
    @patch('src.utils.ejecutar_ejercicios.pd.read_csv')
    @patch('src.utils.ejecutar_ejercicios.os.path.exists', return_value=True)
    @patch('builtins.input', return_value='')
    def test_nombre_default_si_vacio(self, mock_input, mock_exists,
                                     mock_read_csv, mock_generar):
        """Test que usa 'alumno' como nombre por defecto si está vacío"""
        mock_df = pd.DataFrame({'col1': [1, 2]})
        mock_read_csv.return_value = mock_df

        ejecutar_ejercicios.ejecutar_ejercicio3()

        mock_generar.assert_called_once_with(mock_df, 'alumno')


class TestEjecutarEjercicio4(unittest.TestCase):
    """Tests para la función ejecutar_ejercicio4"""

    @patch('src.utils.ejecutar_ejercicios.ejercicio4.analyze_dataset')
    @patch('src.utils.ejecutar_ejercicios.pd.read_csv')
    @patch('src.utils.ejecutar_ejercicios.os.path.exists', return_value=True)
    def test_ejecutar_con_archivo_existente(self, mock_exists, mock_read_csv,
                                            mock_analyze):
        """Test cuando el archivo fusionado existe"""
        mock_df = pd.DataFrame({'col1': [1, 2]})
        mock_read_csv.return_value = mock_df

        ejecutar_ejercicios.ejecutar_ejercicio4()

        mock_exists.assert_called_once_with('data/dataset_fusionado.csv')
        mock_read_csv.assert_called_once_with('data/dataset_fusionado.csv')
        mock_analyze.assert_called_once_with(mock_df)

    @patch('src.utils.ejecutar_ejercicios.ejercicio4.analyze_dataset')
    @patch('src.utils.ejecutar_ejercicios.ejecutar_ejercicio2')
    @patch('src.utils.ejecutar_ejercicios.os.path.exists', return_value=False)
    def test_ejecutar_sin_archivo_ejecuta_ejercicio2(self, mock_exists,
                                                     mock_ejercicio2,
                                                     mock_analyze):
        """Test que ejecuta ejercicio 2 si no existe el archivo"""
        mock_df = pd.DataFrame({'col1': [1, 2]})
        mock_ejercicio2.return_value = mock_df

        ejecutar_ejercicios.ejecutar_ejercicio4()

        mock_exists.assert_called_once()
        mock_ejercicio2.assert_called_once()
        mock_analyze.assert_called_once_with(mock_df)


class TestIntegracionEjerciciosFlow(unittest.TestCase):
    """Tests de integración del flujo de ejercicios"""

    @patch('src.utils.ejecutar_ejercicios.ejercicio4.analyze_dataset')
    @patch('src.utils.ejecutar_ejercicios.ejercicio3.generar_graficos_series_temporales')
    @patch('src.utils.ejecutar_ejercicios.ejercicio2.limpiar_y_fusionar')
    @patch('src.utils.ejecutar_ejercicios.pd.read_excel')
    @patch('src.utils.ejecutar_ejercicios.pd.read_csv')
    @patch('src.utils.ejecutar_ejercicios.os.path.exists', return_value=False)
    @patch('builtins.input')
    def test_flujo_ejercicio3_sin_datos_genera_ejercicio2(self, mock_input,
                                                          mock_exists,
                                                          mock_read_csv,
                                                          mock_read_excel,
                                                          mock_limpiar,
                                                          mock_graficos,
                                                          mock_analyze):
        """Test del flujo: ejercicio 3 sin datos previos ejecuta ejercicio 2"""
        mock_input.return_value = 'TestUser'

        mock_df_rend = pd.DataFrame({'Taxa rendiment': [70.0]})
        mock_df_aban = pd.DataFrame({'% Abandonament a primer curs': [15.0]})
        mock_df_fusionado = pd.DataFrame({
            'Taxa rendiment': [70.0],
            '% Abandonament a primer curs': [15.0]
        })

        mock_read_excel.side_effect = [mock_df_rend, mock_df_aban]
        mock_limpiar.return_value = mock_df_fusionado

        ejecutar_ejercicios.ejecutar_ejercicio3()

        mock_exists.assert_called()
        mock_limpiar.assert_called_once()
        mock_graficos.assert_called_once()


if __name__ == '__main__':
    unittest.main()
