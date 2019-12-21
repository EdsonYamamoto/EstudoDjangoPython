import numpy as np

from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn import metrics

import pandas as pd
import seaborn as sns
import keras

class MachineLearning:
    def Main(self):

        return MachineLearning.BostonAnalizer(object)

    def BostonAnalizer(self):
        X, y = load_boston(return_X_y=True)
        ## utilize os recursos aprendidos no módulo 1 para analisar
        ## se seu modelo tem qualidade e programe o que for necessário a partir desse ponto

        boston_dataset = load_boston()
        dfBoston = pd.DataFrame(boston_dataset.data, columns=boston_dataset.feature_names)
        dfBoston.head()

        dfBoston['MEDV'] = boston_dataset.target

        g = sns.pairplot(dfBoston)

        # use test_size = 0.2, o random_state eu vou alterar depois para um número secreto
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        kf = KFold(n_splits=10, random_state=42)

        scores = []

        for train_index, test_index in kf.split(X):
            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = y[train_index], y[test_index]

            modelo = LinearRegression()
            modelo.fit(X_train, y_train)
            y_pred = modelo.predict(X_test)
            score = np.mean(np.abs((y_test - y_pred) / y_test)) * 100
            scores.append(score)

        scores = np.array(scores)
        return np.sqrt(metrics.mean_squared_error(y_test, y_pred))