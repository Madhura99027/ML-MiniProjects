#IMPORTING LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
df = pd.read_csv("iris.csv")

#------------------------------------------------>

# Split-out validation dataset
array = df.values
X = array[:,0:4]
Y = array[:,4]

#splitting of dataset into training and validation set
validation_size = 0.30
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)


#------------------------------------------------>

#applying logistic regression
from sklearn.linear_model import LogisticRegression
logit = LogisticRegression()
logit.fit(X_train,Y_train)


#saving the model using pickle
import pickle

pickle.dump(logit,open('logistic.pkl','wb'))


#--------------------------------------------->

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
#save the model

pickle.dump(knn,open('knn.pkl','wb'))
 
#-------------------------------------------->

#applying Dtree
from sklearn.tree import DecisionTreeClassifier
dtree = DecisionTreeClassifier()

dtree.fit(X_train, Y_train)

#save the model

pickle.dump(dtree,open('dtree.pkl','wb'))
