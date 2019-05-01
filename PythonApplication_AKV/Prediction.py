from sklearn import datasets
from joblib import load
from os.path import abspath, dirname, join

clf = load('model.joblib')
#filepath = join('PythonApplicaiton_AKV', 'model.joblib')
#print(filepath)
iris = datasets.load_iris()
X, y = iris.data, iris.target
print(X)
print(y)
print ('Hello')
print (clf.predict(X[1:8]) )


