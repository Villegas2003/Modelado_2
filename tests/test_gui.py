import unittest
from src.gui import CalisteniaSimulacionApp
import tkinter as tk

class TestGUI(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.app = CalisteniaSimulacionApp(self.root)

    def test_initialization(self):
        # Verificamos que los controles se inicialicen correctamente
        self.assertEqual(self.app.angulo_codo.get(), 0)
        self.assertEqual(self.app.angulo_hombro.get(), 0)
        self.assertEqual(self.app.angulo_rodilla.get(), 0)

if __name__ == '__main__':
    unittest.main()
