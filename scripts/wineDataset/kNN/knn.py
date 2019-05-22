import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.colors import ListedColormap
import seaborn as sn
import pylab as pl
from mlxtend.plotting import plot_confusion_matrix
# Import LabelEncoder for data encoding
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
# Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix

cm = 0


def knn():
    """knn [Implements kNN algorithm]
    [1 First of all we import our dataset
    2 Next  read dataset to pandas dataframe
    3 The next step is to split our dataset into
    its attributes and labels
    4 We Encode data columns
    5 combinig all data into single listof tuples
    6 To avoid over-fitting, we will divide our dataset into training and test splits, which gives us
     a better idea as to how our algorithm performed during the testing phase.
    7 We generate Model 
    8 We fit our model on the train set using fit() and perform prediction on the test set using predict()]

    :return: [Algorithm accurancy calculation]
    :rtype: [int]
    """

    global cm
    # 1 Importing the Dataset

    file = '../scriptsForPreparingData/CV/train10.csv'
    # file='../../preparedData/updatedFile.csv'

    # Assign colum names to the dataset
    # We use separator delimiter instead
    # names = ['filmId', 'title', 'genre', 'producer', 'actor', 'rating']

    # 2 read dataset to pandas dataframe
    dataset = pd.read_csv(file, sep=',')

    # 3 The next step is to split our dataset into
    # its attributes and labels:

    le = preprocessing.LabelEncoder()
    dataset['actor'] = le.fit_transform(dataset['actor'])
    dataset['genre'] = le.fit_transform(dataset['genre'])
    dataset['producer'] = le.fit_transform(dataset['producer'])

    features = dataset.iloc[:, [0, 2]]

    y = dataset.iloc[:, 4].values

    # 6 To avoid over-fitting, we will divide our dataset into training and test splits, which gives us
    # a better idea as to how our algorithm performed during the testing phase.

    X_train, X_test, y_train, y_test = train_test_split(
        features, y, test_size=0.2)

    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    scaler.fit(X_train)

    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    from sklearn.neighbors import KNeighborsClassifier

    error = []

    # Calculating error for K values between 1 and 40
    for i in range(1, 150):
        knn = KNeighborsClassifier(n_neighbors=i, metric="manhattan")
        knn.fit(X_train, y_train)
        pred_i = knn.predict(X_test)
        error.append(np.mean(pred_i != y_test))
        print(i)
        print(classification_report(y_test, pred_i))
        accuracy = metrics.accuracy_score(y_test, pred_i)
        print(accuracy)

    plt.figure(figsize=(12, 6))
    plt.plot(range(1, 150), error, color='red', linestyle='dashed', marker='o',
             markerfacecolor='blue', markersize=5)
    plt.title('Error Rate K Value')
    plt.xlabel('K Value')
    plt.ylabel('Mean Error')
    plt.show()
    # print(cm)
    # print(classification_report(y_test, y_pred))

    # Model Accuracy, how often is the classifier correct
    # print("Accuracy:",accuracy)
    # return accuracy


knn()

# while knn() < 0.5:
#     knn()

# fig, ax = plot_confusion_matrix(conf_mat=cm,
#                                     colorbar=True,
#                                     show_absolute=False,
#                                     show_normed=True,
#                                     )
# plt.show()
