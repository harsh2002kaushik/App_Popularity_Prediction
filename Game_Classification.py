import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('.EDA_games/Final_games.csv')
print(df.head())

df['game_types'] = LabelEncoder().fit_transform(df['game_types'])

import sklearn 
from sklearn.model_selection import train_test_split

X=df.drop(['editors_choice'],axis=1)              
Y=df['editors_choice'] 

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

from sklearn import tree
from sklearn.metrics import accuracy_score
import graphviz
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.tree import export_graphviz

tree_clf = tree.DecisionTreeClassifier ()
tree_clf.fit(X_train,Y_train)
print(tree_clf.score(X_test,Y_test))

tree_params = {'max_depth':np.arange(3,6,1),'criterion':['entropy','gini']}
tree_search = GridSearchCV(tree_clf,tree_params,scoring='accuracy')        # make it randomized 
tree_search.fit(X_train,Y_train)
tree_best_params = tree_search.best_params_
tree_optimized = tree.DecisionTreeClassifier(criterion = tree_best_params['criterion'], max_depth = tree_best_params['max_depth'])
tree_optimized.fit(X_train,Y_train
print(tree_optimized.score(X_test,Y_test)

dot_data = export_graphviz(tree_optimized,feature_names=X.columns,filled=True)
graphviz.Source(dot_data)

import xgboost as xgb
xgb = xgb.XGBClassifier(random_state=1,learning_rate=0.01)
xgb.fit(X_train, Y_train)
print(xgb.score(X_test,Y_test))

from sklearn import linear_model              
lm = linear_model.SGDClassifier(loss="hinge", penalty="l2")
lm.fit(X_train, Y_train)
print(lm.score(X_train,Y_train))

lm_params = {"loss" : ["hinge", "log", "squared_hinge", "modified_huber"],
                      "alpha": np.arange(0.0001,0.001,0.001) ,
                      "penalty" : ["l2", "l1", "none"],
                      "max_iter":(np.arange(100,1000,100))}                     
lm_search = GridSearchCV(lm_model, param_grid=lm_params)
lm_search.fit(X_train,Y_train)
lm_best_params = lm_search.best_params_
lm_optimized = linear_model.SGDClassifier(loss=lm_best_params['loss'],penalty=lm_best_params['penalty'])
lm_optimized.fit(X_train,Y_train)
print(lm_optimized.score(X_test,Y_test))

from sklearn import svm
svm = svm.SVC()
svm.fit(X_train, Y_train)
print(svm.score(X_train,Y_train))

from sklearn import ensemble
rf = ensemble.RandomForestClassifier()
rf.fit(X_train, Y_train)
print(rf.score(X_test,Y_test))
