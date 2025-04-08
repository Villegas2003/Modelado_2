import unittest
from src.physics import calcular_fuerzas_torques

class TestPhysics(unittest.TestCase):

    def test_calcular_fuerzas_torques(self):
        # Test con valores arbitrarios
        angulo_codo = 90
        angulo_hombro = 45
        angulo_rodilla = 30
        
        fuerzas, torques = calcular_fuerzas_torques(angulo_codo, angulo_hombro, angulo_rodilla)
        
        # Comprobamos que las fuerzas y torques no sean nulos
        self.assertGreater(fuerzas, 0)
        self.assertGreater(torques, 0)

if __name__ == '__main__':
    unittest.main()
