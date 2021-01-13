
import numpy as np
import pandas as pd
from sklearn.ensemble import  RandomForestClassifier
import  pickle


df=pd.read_csv('traina.csv')
to_drop = ['Loan_ID','Gender','Married','Dependents','Education','Self_Employed','Property_Area']
df = df.drop(to_drop,axis=1)
y_train = df['Loan_Status']
X_train = df.drop('Loan_Status',axis=1)


X_train=X_train.fillna(0)

clf=RandomForestClassifier(n_estimators=1000)
clf.fit(X_train,y_train)


pickle.dump(clf,open('model.pkl','wb'))


























