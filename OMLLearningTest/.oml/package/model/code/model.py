"""
Owner: isst
Please implement your own ModelImp
"""
import sys
import os

from OMLLearningTest.model import Model


class ModelImp:
    def  __init__(self):
        print('loading model...')
        # load model
        data_dirpath = os.path.join(os.path.dirname(__file__), '..', 'data')
        self.model = Model(data_dirpath)
        print('model loaded.')

    # string version of Eval
    # data is a string
    def Eval(self, data):
        # Do your implement in following
        return self.model.predict(data)

    # binary version of Eval
    # data is python class "bytes"
    def EvalBinary(self, data):
        return data