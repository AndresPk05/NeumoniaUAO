import unittest
from PDF import PDF
from tkinter import *
from tkinter import ttk, font, filedialog

class TestExportPDF(unittest.TestCase):
    # Método que se ejecuta antes de cada prueba
    def setUp(self):
        self.reportID = 5
        self.root = Tk()

    # Prueba para el método create_pdf de la clase PDF
    def test_create_pdf(self):
        self.assertEqual(PDF.create_pdf(self), "El PDF fue generado con éxito.")


if __name__ == "__main__":
    unittest.main()
