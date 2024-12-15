import unittest
from unittest.mock import patch
from main import (
    ua_to_km, km_to_ua, al_to_km, km_to_al, 
    pc_to_km, km_to_pc, luminosity_from_magnitude,
    main
)

class TestAstronomicalCalculations(unittest.TestCase):

    def test_ua_to_km(self):
        self.assertEqual(ua_to_km(1), 149597870.7)
    
    def test_km_to_ua(self):
        self.assertEqual(km_to_ua(149597870.7), 1)
    
    def test_al_to_km(self):
        self.assertEqual(al_to_km(1), 9.461e12)
    
    def test_km_to_al(self):
        self.assertEqual(km_to_al(9.461e12), 1)
    
    def test_pc_to_km(self):
        self.assertEqual(pc_to_km(1), 3.086e13)
    
    def test_km_to_pc(self):
        self.assertEqual(km_to_pc(3.086e13), 1)

    def test_luminosity_from_magnitude(self):
        luminosity = luminosity_from_magnitude(5, 10)
        self.assertAlmostEqual(luminosity, 0.8550667128846834, places=6)


class TestMainFunction(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', 'a', '10', '3'])  # 3 pour quitter proprement
    @patch('builtins.print')
    def test_main_conversion(self, mock_print, mock_input):
        main()
        #mock_print.assert_any_call("10 UA = 1495978707.00 km")
        mock_print.assert_any_call("Au revoir !")
        self.assertTrue(mock_print.called)

    @patch('builtins.input', side_effect=['2', '5', '10', '3'])
    @patch('builtins.print')
    def test_main_luminosity(self, mock_print, mock_input):
        main()
        mock_print.assert_any_call("Au revoir !")
        self.assertTrue(mock_print.called)

    @patch('builtins.input', side_effect=['3'])
    @patch('builtins.print')
    def test_main_quit(self, mock_print, mock_input):
        main()
        mock_print.assert_any_call("Au revoir !")


class TestInvalidInputs(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', 'x', 'q', '3'])
    @patch('builtins.print')
    def test_invalid_conversion_input(self, mock_print, mock_input):
        main()
        mock_print.assert_any_call("Au revoir !")

    @patch('builtins.input', side_effect=['2', 'x', '3', '10', '3'])
    @patch('builtins.print')
    def test_invalid_luminosity_input(self, mock_print, mock_input):
        main()
        mock_print.assert_any_call("Au revoir !")


if __name__ == '__main__':
    unittest.main()
