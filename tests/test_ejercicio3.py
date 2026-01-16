"""
Tests unitarios para ejercicio4.py
"""

import unittest
from unittest.mock import patch, mock_open
import pandas as pd
import sys
import os
import json

# Importar el módulo a testear
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root_dir)
from src.modules import ejercicio4


class TestAnalyzeDataset(unittest.TestCase):
    """Tests para la función analyze_dataset"""

    def setUp(self):
        """Configuración inicial para cada test"""
        self.df_test = pd.DataFrame({
            'Curs Acadèmic': ['2019-2020', '2020-2021', '2021-2022'] * 3,
            'Branca': ['Ciencias'] * 3 + ['Ingeniería'] * 3 + ['Artes'] * 3,
            '% Abandonament a primer curs':
            [16.0, 15.0, 14.0, 13.0, 12.0, 11.0, 18.0, 17.0, 16.0],
            'Taxa rendiment':
            [68.0, 70.0, 72.0, 73.0, 75.0, 76.0, 65.0, 66.0, 67.0]
        })

    @patch('src.modules.ejercicio4.os.makedirs')
    @patch('builtins.open', new_callable=mock_open)
    @patch('src.modules.ejercicio4.datetime')
    def test_genera_metadata_correcta(self, mock_datetime, mock_file,
                                      mock_makedirs):
        """Test que verifica la generación correcta de metadata"""
        mock_datetime.now.return_value.strftime.return_value = '2024-01-15'

        ejercicio4.analyze_dataset(self.df_test)

        handle = mock_file()
        written_data = ''.join(call.args[0] for call in handle.write.call_args_list)
        resultado = json.loads(written_data)

        self.assertIn('metadata', resultado)
        self.assertEqual(resultado['metadata']['num_registros'], 9)
        self.assertEqual(resultado['metadata']['fecha_analisis'], '2024-01-15')
        self.assertIn('periodo_temporal', resultado['metadata'])

    @patch('src.modules.ejercicio4.os.makedirs')
    @patch('builtins.open', new_callable=mock_open)
    def test_genera_estadisticas_globales(self, mock_file, mock_makedirs):
        """Test que verifica la generación de estadísticas globales"""
        ejercicio4.analyze_dataset(self.df_test)

        handle = mock_file()
        written_data = ''.join(call.args[0] for call in handle.write.call_args_list)
        resultado = json.loads(written_data)

        self.assertIn('estadisticas_globales', resultado)
        globales = resultado['estadisticas_globales']

        self.assertIn('abandono_medio', globales)
        self.assertIn('rendimiento_medio', globales)
        self.assertIn('correlacion_abandono_rendimiento', globales)
        self.assertIsInstance(globales['abandono_medio'], float)
        self.assertIsInstance(globales['rendimiento_medio'], float)
        self.assertIsInstance(globales['correlacion_abandono_rendimiento'], float)

    @patch('src.modules.ejercicio4.os.makedirs')
    @patch('builtins.open', new_callable=mock_open)
    def test_genera_analisis_por_rama(self, mock_file, mock_makedirs):
        """Test que verifica el análisis por rama"""
        ejercicio4.analyze_dataset(self.df_test)
        
        handle = mock_file()
        written_data = ''.join(call.args[0] for call in handle.write.call_args_list)
        resultado = json.loads(written_data)

        self.assertIn('analisis_por_rama', resultado)
        analisis = resultado['analisis_por_rama']

        self.assertIn('Ciencias', analisis)
        self.assertIn('Ingeniería', analisis)
        self.assertIn('Artes', analisis)

        for rama in ['Ciencias', 'Ingeniería', 'Artes']:
            rama_data = analisis[rama]
            self.assertIn('abandono_medio', rama_data)
            self.assertIn('abandono_std', rama_data)
            self.assertIn('abandono_min', rama_data)
            self.assertIn('abandono_max', rama_data)
            self.assertIn('rendimiento_medio', rama_data)
            self.assertIn('rendimiento_std', rama_data)
            self.assertIn('rendimiento_min', rama_data)
            self.assertIn('rendimiento_max', rama_data)
            self.assertIn('tendencia_abandono', rama_data)
            self.assertIn('tendencia_rendimiento', rama_data)

    @patch('src.modules.ejercicio4.os.makedirs')
    @patch('builtins.open', new_callable=mock_open)
    def test_tendencias_correctas(self, mock_file, mock_makedirs):
        """Test que verifica el cálculo correcto de tendencias"""
        df_tendencias = pd.DataFrame({
            'Curs Acadèmic': ['2019-2020', '2020-2021', '2021-2022'],
            'Branca': ['Ciencias'] * 3,
            '% Abandonament a primer curs': [20.0, 15.0, 10.0],
            'Taxa rendiment': [60.0, 70.0, 80.0]
        })

        ejercicio4.analyze_dataset(df_tendencias)

        handle = mock_file()
        written_data = ''.join(call.args[0] for call in handle.write.call_args_list)
        resultado = json.loads(written_data)

        ciencias = resultado['analisis_por_rama']['Ciencias']
        self.assertEqual(ciencias['tendencia_abandono'], 'decreciente')
        self.assertEqual(ciencias['tendencia_rendimiento'], 'creciente')

    @patch('src.modules.ejercicio4.os.makedirs')
    @patch('builtins.open', new_callable=mock_open)
    def test_genera_ranking_ramas(self, mock_file, mock_makedirs):
        """Test que verifica la generación del ranking de ramas"""
        ejercicio4.analyze_dataset(self.df_test)

        handle = mock_file()
        written_data = ''.join(call.args[0] for call in handle.write.call_args_list)
        resultado = json.loads(written_data)

        self.assertIn('ranking_ramas', resultado)
        ranking = resultado['ranking_ramas']

        self.assertIn('mejor_rendimiento', ranking)
        self.assertIn('peor_rendimiento', ranking)
        self.assertIn('mayor_abandono', ranking)
        self.assertIn('menor_abandono', ranking)
        self.assertIsInstance(ranking['mejor_rendimiento'], list)
        self.assertGreater(len(ranking['mejor_rendimiento']), 0)

    @patch('src.modules.ejercicio4.os.makedirs')
    @patch('builtins.open', new_callable=mock_open)
    def test_guarda_archivo_json(self, mock_file, mock_makedirs):
        """Test que verifica que se guarda el archivo JSON correctamente"""
        ejercicio4.analyze_dataset(self.df_test)

        mock_makedirs.assert_called_once_with('src/report', exist_ok=True)
        mock_file.assert_called_once_with(
            'src/report/analisi_estadistic.json',
            'w',
            encoding='utf-8'
        )

    @patch('src.modules.ejercicio4.os.makedirs')
    @patch('builtins.open', new_callable=mock_open)
    def test_estructura_json_completa(self, mock_file, mock_makedirs):
        """Test que verifica la estructura completa del JSON"""
        ejercicio4.analyze_dataset(self.df_test)

        handle = mock_file()
        written_data = ''.join(call.args[0] for call in handle.write.call_args_list)
        resultado = json.loads(written_data)

        self.assertIn('metadata', resultado)
        self.assertIn('estadisticas_globales', resultado)
        self.assertIn('analisis_por_rama', resultado)
        self.assertIn('ranking_ramas', resultado)

    @patch('src.modules.ejercicio4.os.makedirs')
    @patch('builtins.open', new_callable=mock_open)
    def test_valores_numericos_correctos(self, mock_file, mock_makedirs):
        """Test que verifica que los valores numéricos son correctos"""
        df_simple = pd.DataFrame({
            'Curs Acadèmic': ['2020-2021'] * 2,
            'Branca': ['Ciencias', 'Ciencias'],
            '% Abandonament a primer curs': [10.0, 20.0],
            'Taxa rendiment': [60.0, 80.0]
        })

        ejercicio4.analyze_dataset(df_simple)

        handle = mock_file()
        written_data = ''.join(call.args[0] for call in handle.write.call_args_list)
        resultado = json.loads(written_data)

        globales = resultado['estadisticas_globales']
        self.assertAlmostEqual(globales['abandono_medio'], 15.0, places=1)
        self.assertAlmostEqual(globales['rendimiento_medio'], 70.0, places=1)

    def test_manejo_datos_vacios(self):
        """Test con DataFrame vacío"""
        df_vacio = pd.DataFrame(columns=[
            'Curs Acadèmic', 'Branca',
            '% Abandonament a primer curs', 'Taxa rendiment'
        ])

        with patch('builtins.open', mock_open()):
            with patch('src.modules.ejercicio4.os.makedirs'):
                try:
                    ejercicio4.analyze_dataset(df_vacio)
                except Exception as e:
                    self.fail(f"analyze_dataset lanzó excepción con datos vacíos: {e}")

    @patch('src.modules.ejercicio4.os.makedirs')
    @patch('builtins.open', new_callable=mock_open)
    def test_tendencia_estable(self, mock_file, mock_makedirs):
        """Test que verifica identificación de tendencia estable"""
        df_estable = pd.DataFrame({
            'Curs Acadèmic': ['2019-2020', '2020-2021', '2021-2022'],
            'Branca': ['Test'] * 3,
            '% Abandonament a primer curs': [15.0, 15.1, 14.9],
            'Taxa rendiment': [70.0, 70.1, 69.9]
        })

        ejercicio4.analyze_dataset(df_estable)

        handle = mock_file()
        written_data = ''.join(call.args[0] for call in handle.write.call_args_list)
        resultado = json.loads(written_data)

        test_rama = resultado['analisis_por_rama']['Test']
        self.assertEqual(test_rama['tendencia_abandono'], 'estable')
        self.assertEqual(test_rama['tendencia_rendimiento'], 'estable')


if __name__ == '__main__':
    unittest.main()
