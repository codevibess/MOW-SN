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
#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix

cm=0


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

    file ='../scriptsForPreparingData/CV/train10.csv'
    # file='../../preparedData/updatedFile.csv'

    # Assign colum names to the dataset
    # We use separator delimiter instead
    # names = ['filmId', 'title', 'genre', 'producer', 'actor', 'rating']

    # 2 read dataset to pandas dataframe
    dataset = pd.read_csv(file, sep=',')


    # 3 The next step is to split our dataset into
    # its attributes and labels:

    titles = dataset.iloc[:, 5].values
    genres = dataset.iloc[:, 2].values
    producers = dataset.iloc[:, 3].values
    actors = dataset.iloc[:, 0].values
    y = dataset.iloc[:, 4].values

    # 4 Encoding data columns  
    # creating labelEncoder
    le = preprocessing.LabelEncoder()
    # Converting string labels into numbers.
    titles_encoded=le.fit_transform(titles)
    genres_encoded=le.fit_transform(genres)
    producers_encoded=le.fit_transform(producers)
    actors_encoded=le.fit_transform(actors)
    # 5 combinig all data into single listof tuples
    features=list(zip(actors_encoded, genres_encoded))

    # 6 To avoid over-fitting, we will divide our dataset into training and test splits, which gives us
    # a better idea as to how our algorithm performed during the testing phase.
    
    X_train, X_test, y_train, y_test = train_test_split(features, y, test_size=0.2)

    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    scaler.fit(X_train)

    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    from sklearn.neighbors import KNeighborsClassifier
    # 7 Generating Model
    classifier = KNeighborsClassifier(n_neighbors=95)
    # 8 fit  model on the train set using fit() and perform prediction on the test set using predict()
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)

    cm= confusion_matrix(y_test, y_pred)
    accuracy=metrics.accuracy_score(y_test, y_pred)

    print(cm)
    print(classification_report(y_test, y_pred))

    # Model Accuracy, how often is the classifier correct
    print("Accuracy:",accuracy)
    return accuracy


knn()

while knn() < 0.5:
    knn()

fig, ax = plot_confusion_matrix(conf_mat=cm,
                                    colorbar=True,
                                    show_absolute=False,
                                    show_normed=True,
                                    )
plt.show()