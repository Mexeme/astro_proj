import unittest
from main import (
    ua_to_km, km_to_ua, al_to_km, km_to_al, 
    pc_to_km, km_to_pc, luminosity_from_magnitude
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

if __name__ == "__main__":
    unittest.main()
