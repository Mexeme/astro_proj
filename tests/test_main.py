import unittest
from unittest.mock import patch
from main import (
    ua_to_km, km_to_ua, al_to_km, km_to_al, 
    pc_to_km, km_to_pc, luminosity_from_magnitude,
    main
)

class TestAstronomicalCalculations(unittest.TestCase):

    # Test des conversions d'unités
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

    # Test du calcul de luminosité
    def test_luminosity_from_magnitude(self):
        # Exemple de test avec magnitude = 5 et distance = 10 parsecs
        luminosity = luminosity_from_magnitude(5, 10)
        self.assertAlmostEqual(luminosity, 0.8550667128846834, places=6)


class TestMainFunction(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', 'a', '10', '2', '5', '10', '3'])
    @patch('builtins.print')
    def test_main_conversion(self, mock_print, mock_input):
        """Test de la conversion d'unités via la fonction main."""
        main()  # Appeler la fonction principale
        mock_print.assert_called_with("10 UA = 1495978707.0 km")  # Vérification de l'affichage du résultat de conversion

    @patch('builtins.input', side_effect=['2', '5', '10', '3'])
    @patch('builtins.print')
    def test_main_luminosity(self, mock_print, mock_input):
        """Test du calcul de la luminosité d'une étoile via la fonction main."""
        main()  # Appeler la fonction principale
        mock_print.assert_called_with("La luminosité de l'étoile est de 0.8550667128846834 fois la luminosité du Soleil.")  # Vérification du calcul de luminosité

    @patch('builtins.input', side_effect=['3'])  # Tester l'option Quitter
    @patch('builtins.print')
    def test_main_quit(self, mock_print, mock_input):
        """Test de l'option quitter de la fonction main."""
        main()  # Appeler la fonction principale
        mock_print.assert_called_with("Au revoir!")  # Vérification du message de fin de programme


class TestInvalidInputs(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', 'a', '10', '3'])
    @patch('builtins.print')
    def test_invalid_conversion_input(self, mock_print, mock_input):
        """Test des entrées invalides pour la conversion d'unités."""
        main()
        mock_print.assert_called_with("Erreur : Veuillez entrer un nombre valide.")  # Vérifier le message d'erreur pour l'entrée invalide

    @patch('builtins.input', side_effect=['2', 'a', '10', '3'])
    @patch('builtins.print')
    def test_invalid_luminosity_input(self, mock_print, mock_input):
        """Test des entrées invalides pour la luminosité d'étoile."""
        main()
        mock_print.assert_called_with("Erreur : Veuillez entrer un nombre valide.")  # Vérifier le message d'erreur pour l'entrée invalide


if __name__ == '__main__':
    unittest.main()
