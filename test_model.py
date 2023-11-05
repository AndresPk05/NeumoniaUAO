import unittest
from Image import ImageFile
import PredictNeomony

class TestModel(unittest.TestCase):
    def setUp(self):
        self.image = ImageFile()
        self.filepath = "viral (3).dcm"

    def test_predict_neomony(self):
        array, img2show = self.image.read_dicom_file(self.filepath)
        label, proba, heatmap = PredictNeomony.predict(array)
        self.assertEqual(label, "viral")
        self.assertEqual(proba, 88.81623148918152)


if __name__ == "__main__":
    unittest.main()

