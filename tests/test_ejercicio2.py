"""
Tests unitarios para ejercicio2.py
"""

import unittest
from unittest.mock import patch
import pandas as pd
import sys
import os

# Importar el módulo a testear
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root_dir)
from src.modules import ejercicio2


class TestRenombrarColumnasAbandono(unittest.TestCase):
    """Tests para la función renombrar_columnas_abandono"""

    def test_renombrar_columnas_correcto(self):
        """Test renombrado correcto de columnas"""
        df_original = pd.DataFrame({
            'Naturalesa universitat responsable': [1, 2],
            'Universitat Responsable': ['A', 'B'],
            'Sexe Alumne': ['M', 'F'],
            'Tipus de centre': ['Si', 'No'],
            'Otra_Columna': [10, 20]
        })

        resultado = ejercicio2.renombrar_columnas_abandono(df_original)

        self.assertIn('Tipus universitat', resultado.columns)
        self.assertIn('Universitat', resultado.columns)
        self.assertIn('Sexe', resultado.columns)
        self.assertIn('Integrat S/N', resultado.columns)
        self.assertNotIn('Naturalesa universitat responsable', resultado.columns)
        self.assertNotIn('Universitat Responsable', resultado.columns)
        self.assertNotIn('Sexe Alumne', resultado.columns)
        self.assertNotIn('Tipus de centre', resultado.columns)
        self.assertIn('Otra_Columna', resultado.columns)


class TestEliminarColumnas(unittest.TestCase):
    """Tests para la función eliminar_columnas"""

    def test_eliminar_columnas_existentes(self):
        """Test eliminación de columnas que existen"""
        df_rendimiento = pd.DataFrame({
            'Universitat': ['A', 'B'],
            'Unitat': [1, 2],
            'Crèdits ordinaris superats': [30, 40],
            'Crèdits ordinaris matriculats': [60, 60],
            'Taxa rendiment': [50.0, 66.7]
        })

        df_abandono = pd.DataFrame({
            'Universitat': ['A', 'B'],
            'Unitat': [1, 2],
            '% Abandonament a primer curs': [10.0, 15.0]
        })

        rend_limpio, aban_limpio = ejercicio2.eliminar_columnas(
            df_rendimiento, df_abandono
        )

        self.assertNotIn('Universitat', rend_limpio.columns)
        self.assertNotIn('Unitat', rend_limpio.columns)
        self.assertNotIn('Crèdits ordinaris superats', rend_limpio.columns)
        self.assertNotIn('Crèdits ordinaris matriculats', rend_limpio.columns)
        self.assertIn('Taxa rendiment', rend_limpio.columns)
        self.assertNotIn('Universitat', aban_limpio.columns)
        self.assertNotIn('Unitat', aban_limpio.columns)
        self.assertIn('% Abandonament a primer curs', aban_limpio.columns)

    def test_eliminar_columnas_no_existentes(self):
        """Test que no falla si las columnas no existen"""
        df_rendimiento = pd.DataFrame({
            'Taxa rendiment': [50.0, 66.7]
        })

        df_abandono = pd.DataFrame({
            '% Abandonament a primer curs': [10.0, 15.0]
        })

        rend_limpio, aban_limpio = ejercicio2.eliminar_columnas(
            df_rendimiento, df_abandono
        )

        self.assertEqual(len(rend_limpio.columns), 1)
        self.assertEqual(len(aban_limpio.columns), 1)


class TestAgruparPorCaracteristicas(unittest.TestCase):
    """Tests para la función agrupar_por_caracteristicas"""

    def test_agrupar_calcula_media_correcta(self):
        """Test que agrupa correctamente y calcula la media"""
        df = pd.DataFrame({
            'Curs Acadèmic': ['2020-2021', '2020-2021', '2021-2022'],
            'Tipus universitat': ['Pública', 'Pública', 'Privada'],
            'Sigles': ['UB', 'UB', 'UAO'],
            'Tipus Estudi': ['Grado', 'Grado', 'Grado'],
            'Branca': ['Ciencias', 'Ciencias', 'Ingeniería'],
            'Sexe': ['Hombre', 'Hombre', 'Mujer'],
            'Integrat S/N': ['Sí', 'Sí', 'No'],
            'Taxa rendiment': [60.0, 80.0, 90.0]
        })

        resultado = ejercicio2.agrupar_por_caracteristicas(df, 'Taxa rendiment')

        self.assertEqual(len(resultado), 2)
        primer_grupo = resultado[resultado['Curs Acadèmic'] == '2020-2021']
        self.assertEqual(primer_grupo['Taxa rendiment'].values[0], 70.0)

    def test_agrupar_con_columnas_faltantes(self):
        """Test con columnas que no existen en el DataFrame"""
        df = pd.DataFrame({
            'Curs Acadèmic': ['2020-2021', '2020-2021'],
            'Branca': ['Ciencias', 'Ciencias'],
            'Taxa rendiment': [60.0, 80.0]
        })

        resultado = ejercicio2.agrupar_por_caracteristicas(df, 'Taxa rendiment')

        self.assertIsInstance(resultado, pd.DataFrame)
        self.assertIn('Taxa rendiment', resultado.columns)


class TestFusionarDatasets(unittest.TestCase):
    """Tests para la función fusionar_datasets"""

    def test_fusionar_inner_join_correcto(self):
        """Test fusión con inner join"""
        df_rendimiento = pd.DataFrame({
            'Curs Acadèmic': ['2020-2021', '2021-2022', '2022-2023'],
            'Branca': ['Ciencias', 'Ingeniería', 'Artes'],
            'Taxa rendiment': [70.0, 80.0, 75.0]
        })

        df_abandono = pd.DataFrame({
            'Curs Acadèmic': ['2020-2021', '2021-2022'],
            'Branca': ['Ciencias', 'Ingeniería'],
            '% Abandonament a primer curs': [15.0, 12.0]
        })

        resultado = ejercicio2.fusionar_datasets(df_rendimiento, df_abandono)

        self.assertEqual(len(resultado), 2)
        self.assertIn('Taxa rendiment', resultado.columns)
        self.assertIn('% Abandonament a primer curs', resultado.columns)
        ciencias = resultado[resultado['Branca'] == 'Ciencias']
        self.assertEqual(ciencias['Taxa rendiment'].values[0], 70.0)
        self.assertEqual(ciencias['% Abandonament a primer curs'].values[0], 15.0)


class TestLimpiarYFusionar(unittest.TestCase):
    """Tests para la función limpiar_y_fusionar"""

    @patch('src.modules.ejercicio2.os.path.exists', return_value=True)
    @patch('src.modules.ejercicio2.os.makedirs')
    @patch('pandas.DataFrame.to_csv')
    def test_limpiar_y_fusionar_proceso_completo(self, mock_to_csv,
                                                 mock_makedirs, mock_exists):
        """Test del proceso completo de limpieza y fusión"""
        df_rendimiento = pd.DataFrame({
            'Curs Acadèmic': ['2020-2021', '2020-2021'],
            'Tipus universitat': ['Pública', 'Pública'],
            'Universitat': ['UB', 'UB'],
            'Unitat': [1, 1],
            'Sigles': ['UB', 'UB'],
            'Tipus Estudi': ['Grado', 'Grado'],
            'Branca': ['Ciencias', 'Ciencias'],
            'Sexe': ['Hombre', 'Mujer'],
            'Integrat S/N': ['Sí', 'Sí'],
            'Crèdits ordinaris superats': [30, 40],
            'Crèdits ordinaris matriculats': [60, 60],
            'Taxa rendiment': [50.0, 66.7]
        })

        df_abandono = pd.DataFrame({
            'Curs Acadèmic': ['2020-2021', '2020-2021'],
            'Naturalesa universitat responsable': ['Pública', 'Pública'],
            'Universitat Responsable': ['UB', 'UB'],
            'Unitat': [1, 1],
            'Sigles': ['UB', 'UB'],
            'Tipus Estudi': ['Grado', 'Grado'],
            'Branca': ['Ciencias', 'Ciencias'],
            'Sexe Alumne': ['Hombre', 'Mujer'],
            'Tipus de centre': ['Sí', 'Sí'],
            '% Abandonament a primer curs': [10.0, 15.0]
        })

        resultado = ejercicio2.limpiar_y_fusionar(df_rendimiento, df_abandono)

        self.assertIsInstance(resultado, pd.DataFrame)
        self.assertIn('Taxa rendiment', resultado.columns)
        self.assertIn('% Abandonament a primer curs', resultado.columns)
        mock_to_csv.assert_called_once()

    @patch('src.modules.ejercicio2.os.path.exists', return_value=False)
    @patch('src.modules.ejercicio2.os.makedirs')
    @patch('pandas.DataFrame.to_csv')
    def test_crear_directorio_si_no_existe(self, mock_to_csv, mock_makedirs,
                                           mock_exists):
        """Test que crea el directorio data si no existe"""
        df_rendimiento = pd.DataFrame({
            'Curs Acadèmic': ['2020-2021'],
            'Tipus universitat': ['Pública'],
            'Sigles': ['UB'],
            'Tipus Estudi': ['Grado'],
            'Branca': ['Ciencias'],
            'Sexe': ['Hombre'],
            'Integrat S/N': ['Sí'],
            'Taxa rendiment': [50.0]
        })

        df_abandono = pd.DataFrame({
            'Curs Acadèmic': ['2020-2021'],
            'Tipus universitat': ['Pública'],
            'Sigles': ['UB'],
            'Tipus Estudi': ['Grado'],
            'Branca': ['Ciencias'],
            'Sexe': ['Hombre'],
            'Integrat S/N': ['Sí'],
            '% Abandonament a primer curs': [10.0]
        })

        ejercicio2.limpiar_y_fusionar(df_rendimiento, df_abandono)

        mock_makedirs.assert_called_once_with('data')


if __name__ == '__main__':
    unittest.main()
