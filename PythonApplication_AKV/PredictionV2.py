import pandas
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib

#testinputnames = 'preg,plas,pres,skin,test,mass,pedi,age,class'
#testinputnames = 'apple,able,as,skin,test,mass,pig,shut,class'

#names = testinputnames.split(',')
#print(names)
#url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
#names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

#dataframe = pandas.read_csv(url, names=names)

dataframe = pandas.read_csv('inputdata.txt', names=['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class'])

array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
test_size = 0.33
seed = 7
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)

# load the model from disk
filename = 'finalized_model_v2.sav'
loaded_model = joblib.load(filename)

# Score
result = loaded_model.predict(X_test)
print(len(X_test))
print(type(result))
print(str(result))

# Predict
Xnew = [[6,148,72,35,0,33.6,0.627,50]]
ynew = loaded_model.predict(Xnew)
print("X=%s, Predicted=%s" % (Xnew[0], ynew[0]))


