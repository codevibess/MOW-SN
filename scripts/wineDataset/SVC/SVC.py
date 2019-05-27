import pandas as pd
from sklearn.model_selection import KFold, cross_val_score, cross_val_predict
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix

name_file = '../../../preparedData/wineDataset/wines_scaled.csv'

data = pd.read_csv(name_file, sep=',')

features = data.iloc[:, 1:12]
y = data.iloc[:, 12].values

scores = []

best_svc = SVC(gamma='auto')
cv = KFold(n_splits=10, shuffle=False)

# X = features.values

scaler = StandardScaler()
X = scaler.fit_transform(features)

for train_index, test_index in cv.split(X):
    print("Train Index: ", train_index, "\n")
    print("Test Index: ", test_index)

    X_train, X_test, y_train, y_test = X[train_index], X[test_index], y[train_index], y[test_index]
    best_svc.fit(X_train, y_train)
    scores.append(best_svc.score(X_test, y_test))

    y_predict = best_svc.predict(X_test)
    print(confusion_matrix(y_test, y_predict))
    print(classification_report(y_test, y_predict))

result = cross_val_score(best_svc, X, y, cv=10)
sum_result = sum(result)
print('sum res->', sum_result/10)
print(np.mean(scores))
print(cross_val_score(best_svc, X, y, cv=10))
print(cross_val_predict(best_svc, X, y, cv=10))
