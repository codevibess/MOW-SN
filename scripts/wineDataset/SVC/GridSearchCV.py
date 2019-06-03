import pandas as pd
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn import preprocessing
import numpy as np


def create_grid_search():
    name_file = '../../../preparedData/wineDataset/wines_scaled.csv'

    data = pd.read_csv(name_file, sep=',')

    features = data.iloc[:, 1:12]
    y = data.iloc[:, 12].values

    scaler = StandardScaler()
    X = scaler.fit_transform(features)

    classifier = SVC(kernel='rbf')



    parameters = [{'C': [20.67, 20.69, 20.71, 20.73, 20.79, 20.81],
                   'kernel': ['rbf'],
                   'gamma': [1.338, 1.339, 1.34, 1.341, 1.342]}]

    grid_search = GridSearchCV(estimator=classifier, param_grid=parameters, scoring='accuracy', cv=10, n_jobs=-1)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)



    grid_search = grid_search.fit(X_train, y_train)

    y_pred = grid_search.predict(X_test)

    scores = grid_search.cv_results_
    best_accuracy = grid_search.best_score_
    best_parameters = grid_search.best_params_
    print('Scores -> ', scores)
    print('Best accuracy -> ', best_accuracy)
    print('Best parameters -> ', best_parameters)
    print('conf matrix', confusion_matrix(y_test, y_pred))


if __name__ == '__main__':
    create_grid_search()
