from unittest import TestCase

from .settings import PREDICTION_FILE_PATH
from LearnOMLSampleCode.model import Model


class PredictTest(TestCase):

    def test_predict(self):
        model = Model()
        with open(PREDICTION_FILE_PATH, 'r') as f:
            for row in f:
                data, expected = row.strip().split('\t')
                result = model.predict(data)

                self.assertEqual(result, expected)