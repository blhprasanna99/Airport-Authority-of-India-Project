from sklearn import preprocessing 
import numpy as np
from sklearn.preprocessing import LabelEncoder
from pandas import read_csv
from sklearn.metrics import roc_curve
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import pandas as pd
import matplotlib.pyplot as plt

data1 = pd.read_csv('C:\\Users\\Lekhasree Uddanti\\Desktop\\project\\DelhiAirportData.csv')
data2 = pd.read_csv('C:\\Users\\Lekhasree Uddanti\\Desktop\\project\\GannavaramAirportData.csv')
data3 = pd.read_csv('C:\\Users\\Lekhasree Uddanti\\Desktop\\project\\HyderabadAirportData.csv')
dataset = pd.concat([data1,data2,data3],axis=0)
print(dataset['Service Used'].unique())
print()
print(dataset.groupby('Service Used').size())
print()
print(dataset.groupby('Airport Name').size())
import seaborn as sns
sns.countplot(dataset['Service Used'],label="Count")
plt.show()
label_encoder = preprocessing.LabelEncoder()
#dataset['Service Used']= label_encoder.fit_transform(dataset['Service Used']) 
dataset['Airport Name']= label_encoder.fit_transform(dataset['Airport Name'])
array = dataset.values
X = array[:,[0,2]]
Y = array[:,3]
X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y, test_size=0.20, random_state=1, shuffle=True) 
# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('DT', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('RF',RandomForestClassifier()))
models.append(('SVM', SVC(gamma='auto')))
# evaluate each model in turn
results = []
names = []
for name, model in models:
	kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
	cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
	results.append(cv_results)
	names.append(name)
	print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))
# Compare Algorithms
pyplot.boxplot(results, labels=names)
pyplot.title('Algorithm Comparison')
pyplot.show()
# Make predictions on validation dataset
model = SVC(gamma='auto')
model.fit(X_train, Y_train)
predictions = model.predict(X_validation)
# Evaluate predictions
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))