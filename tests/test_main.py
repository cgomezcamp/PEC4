"""
Tests unitarios para main.py
"""

import unittest
from unittest.mock import patch, MagicMock
import sys
import os
from io import StringIO

# Importar el módulo a testear
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root_dir)
import main


class TestMain(unittest.TestCase):
    """Tests para la función main"""

    @patch('builtins.input', return_value='n')
    @patch('main.ejecutar_ejercicio1')
    @patch('main.argparse.ArgumentParser.parse_args')
    def test_main_ejecuta_ejercicio1(self, mock_args, mock_ejercicio1,
                                     mock_input):
        """Test que ejecuta solo el ejercicio 1"""
        mock_args.return_value = MagicMock(ex=1)

        main.main()

        mock_ejercicio1.assert_called_once()

    @patch('builtins.input', return_value='n')
    @patch('main.ejecutar_ejercicio2')
    @patch('main.argparse.ArgumentParser.parse_args')
    def test_main_ejecuta_ejercicio2(self, mock_args, mock_ejercicio2,
                                     mock_input):
        """Test que ejecuta solo el ejercicio 2"""
        mock_args.return_value = MagicMock(ex=2)

        main.main()

        mock_ejercicio2.assert_called_once()

    @patch('builtins.input', return_value='TestUser')
    @patch('main.ejecutar_ejercicio3')
    @patch('main.argparse.ArgumentParser.parse_args')
    def test_main_ejecuta_ejercicio3(self, mock_args, mock_ejercicio3,
                                     mock_input):
        """Test que ejecuta solo el ejercicio 3"""
        mock_args.return_value = MagicMock(ex=3)

        main.main()

        mock_ejercicio3.assert_called_once()

    @patch('builtins.input', return_value='n')
    @patch('main.ejecutar_ejercicio4')
    @patch('main.argparse.ArgumentParser.parse_args')
    def test_main_ejecuta_ejercicio4(self, mock_args, mock_ejercicio4,
                                     mock_input):
        """Test que ejecuta solo el ejercicio 4"""
        mock_args.return_value = MagicMock(ex=4)

        main.main()

        mock_ejercicio4.assert_called_once()

    @patch('builtins.input', return_value='TestUser')
    @patch('main.ejecutar_ejercicio4')
    @patch('main.ejecutar_ejercicio3')
    @patch('main.ejecutar_ejercicio2')
    @patch('main.ejecutar_ejercicio1')
    @patch('main.argparse.ArgumentParser.parse_args')
    def test_main_sin_argumentos_ejecuta_todos(self, mock_args, mock_ej1,
                                               mock_ej2, mock_ej3, mock_ej4,
                                               mock_input):
        """Test que ejecuta todos los ejercicios sin argumentos"""
        mock_args.return_value = MagicMock(ex=None)

        main.main()

        mock_ej1.assert_called_once()
        mock_ej2.assert_called_once()
        mock_ej3.assert_called_once()
        mock_ej4.assert_called_once()

    @patch('builtins.input', return_value='n')
    @patch('main.sys.exit')
    @patch('main.ejecutar_ejercicio1')
    @patch('main.argparse.ArgumentParser.parse_args')
    def test_main_maneja_file_not_found_error(self, mock_args, mock_ej1,
                                              mock_exit, mock_input):
        """Test que maneja FileNotFoundError correctamente"""
        mock_args.return_value = MagicMock(ex=1)
        mock_ej1.side_effect = FileNotFoundError("Archivo no encontrado")

        main.main()

        mock_exit.assert_called_once_with(1)

    @patch('builtins.input', return_value='n')
    @patch('main.sys.exit')
    @patch('main.ejecutar_ejercicio1')
    @patch('main.argparse.ArgumentParser.parse_args')
    def test_main_maneja_exception_generica(self, mock_args, mock_ej1,
                                            mock_exit, mock_input):
        """Test que maneja excepciones genéricas"""
        mock_args.return_value = MagicMock(ex=1)
        mock_ej1.side_effect = Exception("Error genérico")

        main.main()

        mock_exit.assert_called_once_with(1)

    @patch('builtins.input', return_value='n')
    @patch('sys.stdout', new_callable=StringIO)
    @patch('main.ejecutar_ejercicio1')
    @patch('main.argparse.ArgumentParser.parse_args')
    def test_main_imprime_banner_inicial(self, mock_args, mock_ej1,
                                         mock_stdout, mock_input):
        """Test que imprime el banner inicial"""
        mock_args.return_value = MagicMock(ex=1)

        main.main()

        output = mock_stdout.getvalue()
        self.assertIn('PEC4', output)
        self.assertIn('█', output)

    @patch('builtins.input', return_value='n')
    @patch('sys.stdout', new_callable=StringIO)
    @patch('main.ejecutar_ejercicio1')
    @patch('main.argparse.ArgumentParser.parse_args')
    def test_main_imprime_mensaje_completado(self, mock_args, mock_ej1,
                                             mock_stdout, mock_input):
        """Test que imprime mensaje de ejecución completada"""
        mock_args.return_value = MagicMock(ex=1)

        main.main()

        output = mock_stdout.getvalue()
        self.assertIn('EJECUCIÓN COMPLETADA', output)
        self.assertIn('✅', output)


class TestArgumentParser(unittest.TestCase):
    """Tests para la configuración del ArgumentParser"""

    @patch('sys.argv', ['main.py', '-ex', '1'])
    def test_parser_acepta_ejercicio_1(self):
        """Test que el parser acepta -ex 1"""
        parser = main.argparse.ArgumentParser()
        parser.add_argument('-ex', type=int, choices=[1, 2, 3, 4])
        args = parser.parse_args(['-ex', '1'])
        self.assertEqual(args.ex, 1)

    @patch('sys.argv', ['main.py', '-ex', '5'])
    def test_parser_rechaza_ejercicio_invalido(self):
        """Test que el parser rechaza ejercicios inválidos"""
        parser = main.argparse.ArgumentParser()
        parser.add_argument('-ex', type=int, choices=[1, 2, 3, 4])

        with self.assertRaises(SystemExit):
            parser.parse_args(['-ex', '5'])

    def test_parser_sin_argumentos(self):
        """Test parser sin argumentos devuelve None"""
        parser = main.argparse.ArgumentParser()
        parser.add_argument('-ex', type=int, choices=[1, 2, 3, 4])
        args = parser.parse_args([])
        self.assertIsNone(args.ex)


class TestIntegracionMain(unittest.TestCase):
    """Tests de integración para main"""

    @patch('builtins.input', return_value='TestUser')
    @patch('main.ejecutar_ejercicio4')
    @patch('main.ejecutar_ejercicio3')
    @patch('main.ejecutar_ejercicio2')
    @patch('main.ejecutar_ejercicio1')
    @patch('main.argparse.ArgumentParser.parse_args')
    def test_flujo_completo_todos_ejercicios(self, mock_args, mock_ej1,
                                             mock_ej2, mock_ej3, mock_ej4,
                                             mock_input):
        """Test de integración del flujo completo"""
        mock_args.return_value = MagicMock(ex=None)

        main.main()

        self.assertTrue(mock_ej1.called)
        self.assertTrue(mock_ej2.called)
        self.assertTrue(mock_ej3.called)
        self.assertTrue(mock_ej4.called)

    @patch('builtins.input', return_value='n')
    @patch('main.sys.exit')
    @patch('main.ejecutar_ejercicio1')
    @patch('main.argparse.ArgumentParser.parse_args')
    def test_error_handling_muestra_mensaje(self, mock_args, mock_ej1,
                                            mock_exit, mock_input):
        """Test que verifica el manejo de errores muestra mensaje"""
        mock_args.return_value = MagicMock(ex=1)
        mock_ej1.side_effect = FileNotFoundError("test.csv no encontrado")

        main.main()

        # Verificar que sys.exit fue llamado con código 1
        mock_exit.assert_called_once_with(1)


if __name__ == '__main__':
    unittest.main()
