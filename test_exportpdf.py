import unittest
import ExportPDF	
from tkinter import *
from tkinter import ttk, font, filedialog

class TestExportPDF(unittest.TestCase):
    def setUp(self):
        self.reportID = 5
        self.root = Tk()


    def test_create_pdf(self):
        self.assertEqual(ExportPDF.create_pdf(self), "El PDF fue generado con éxito.")


if __name__ == "__main__":
    unittest.main()
