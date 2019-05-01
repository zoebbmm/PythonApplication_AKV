"""
Implement model's featurization code in this class.
"""
from . import BaseModel


class Model(BaseModel):
    """
    Class for OfficeML Python models. Streamlines the workflow for testing and pushing models into production.
    """

    def __init__(self, data_dirpath=None):
        """
        Model constructor is used to create a representation of the Model associated with the
        data_dirpath argument and load other static files necessary for the deployment of the model.

        :param data_dirpath: The path of the directory where data for the model is stored.
        """
        super().__init__(data_dirpath)

    def predict(self, data):
        """
        Predict a given value based on the trained model.

        :param data: Input value.
        :return: The model's predictions.
        """
        return 'Hello {}!'.format(data)

    def eval(self, **kwargs):
        """
        Batch scoring on the trained model.

        :param kwargs: Extra parameters passed to the model.
        """
        self.generate_scores(0, 0)
