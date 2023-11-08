import tkcap
from PIL import ImageTk, Image

class PDF:
        # Método para crear un PDF a partir de una captura de pantalla
        def create_pdf(this, self):
                cap = tkcap.CAP(self.root)
                ID = "Reporte" + str(self.reportID) + ".jpg"
                img = cap.capture(ID)
                img = Image.open(ID)
                img = img.convert("RGB")
                pdf_path = r"Reporte" + str(self.reportID) + ".pdf"
                img.save(pdf_path)
                self.reportID += 1
                # Devuelve un mensaje de éxito
                return "El PDF fue generado con éxito."