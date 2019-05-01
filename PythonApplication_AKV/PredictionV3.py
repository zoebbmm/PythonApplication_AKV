import pandas
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib

dataframe = pandas.read_csv('inputdata_2d.txt', names=['preg', 'plas', 'class'])
array = dataframe.values
#X = array[:,0:8]
#Y = array[:,8]
#test_size = 0.33
#seed = 7
#X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)


X = array[:,0:2]
Y = array[:,2]

# load the model from disk
filename = 'finalized_model.sav'
loaded_model = joblib.load(filename)
#result = loaded_model.score(X_test, Y_test)
#print(type(result))
#print(str(result))

Xnew = [[-0.79415228, 2.10495117]]
ynew = loaded_model.predict(Xnew)
print("X=%s, Predicted=%s" % (Xnew[0], ynew[0]))


