#IMPORTING LIBRARIES
 #IMPORTING LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn import metrics
import statsmodels.api as sm 

 
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
df = pd.read_csv("data.csv")

#------------------------------------------------>
#Cleaning, Standardization, Normalisation
lb = preprocessing.LabelBinarizer()

df. driveway = lb.fit_transform(df.driveway)
df. recroom = lb.fit_transform(df.recroom)
df. fullbase = lb.fit_transform(df.fullbase)
df. gashw = lb.fit_transform(df.gashw)
df. airco = lb.fit_transform(df.airco)
df. prefarea = lb.fit_transform(df.prefarea)
 
#------------------------------------------------>
#one hot encoding or Dummy variables
df_stories = pd.get_dummies(df['stories'],prefix = 'stories')


#------------------------------------------------>
df = pd.concat([df, df_stories], axis = 1)   #axis= 1 means add column wise
del df['stories']

y=df['price']
independent_variables = ['lotsize', 'bathrms', 'driveway', 'fullbase', 'gashw', 'airco', 'garagepl', 'prefarea', 'stories_four', 'stories_two','stories_one', 'stories_three']

x = df[independent_variables]


#splitting of dataset into training and validation set
validation_size = 0.30
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(x, y, test_size=validation_size, random_state=seed)


a = sm.OLS(Y_train,X_train).fit()


import pickle

pickle.dump(a,open('OLS.pkl','wb'))