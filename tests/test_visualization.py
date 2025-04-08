import unittest
from src.visualization import actualizar_simulacion
import matplotlib.pyplot as plt

class TestVisualization(unittest.TestCase):

    def test_actualizar_simulacion(self):
        # Verificamos que la función no lance errores con valores arbitrarios
        fuerzas = 10
        torques = 5
        try:
            actualizar_simulacion(fuerzas, torques)
        except Exception as e:
            self.fail(f"La función lanzó una excepción: {e}")
        
        # Comprobamos que una figura de matplotlib ha sido creada
        plt.gcf()  # Obtener la figura actual
        self.assertIsNotNone(plt.gcf(), "No se generó una figura de matplotlib")

if __name__ == '__main__':
    unittest.main()
