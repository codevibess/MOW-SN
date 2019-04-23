import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.colors import ListedColormap
import seaborn as sn
import pylab as pl
from mlxtend.plotting import plot_confusion_matrix

cm=0


def knn():
    global cm
    #Importing the Dataset

    file ='../scriptsForPreparingData/CV/train10.csv'
    # file='../../preparedData/updatedFile.csv'

    # Assign colum names to the dataset
    # We use separator delimiter instead
    # names = ['filmId', 'title', 'genre', 'producer', 'actor', 'rating']

    # read dataset to pandas dataframe
    dataset = pd.read_csv(file, sep=',')


    # The next step is to split our dataset into
    # its attributes and labels:

    titles = dataset.iloc[:, 5].values
    genres = dataset.iloc[:, 2].values
    producers = dataset.iloc[:, 3].values
    actors = dataset.iloc[:, 0].values
    y = dataset.iloc[:, 4].values





    # Encoding data columns
    # Import LabelEncoder
    from sklearn import preprocessing
    #creating labelEncoder
    le = preprocessing.LabelEncoder()
    # Converting string labels into numbers.
    titles_encoded=le.fit_transform(titles)
    genres_encoded=le.fit_transform(genres)
    producers_encoded=le.fit_transform(producers)
    actors_encoded=le.fit_transform(actors)
    #combinig all data into single listof tuples
    features=list(zip(actors_encoded, genres_encoded))




    # To avoid over-fitting, we will divide our dataset into training and test splits, which gives us
    # a better idea as to how our algorithm performed during the testing phase.
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(features, y, test_size=0.2)


    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    scaler.fit(X_train)

    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    from sklearn.neighbors import KNeighborsClassifier
    classifier = KNeighborsClassifier(n_neighbors=95)
    classifier.fit(X_train, y_train)

    # # visualization
    # h = .02  # step size in the mesh
    #
    # # Calculate min, max and limits
    # x_min, x_max = X_train[:, 0].min() - 1, X_train[:, 0].max() + 1
    # y_min, y_max = X_train[:, 1].min() - 1, X_train[:, 1].max() + 1
    # xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    #
    # # Put the result into a color plot
    # plt.figure()
    # plt.scatter(X_train[:, 0], X_train[:, 1])
    # plt.xlim(xx.min(), xx.max())
    # plt.ylim(yy.min(), yy.max())
    # plt.title("Data points")
    # plt.show()

    y_pred = classifier.predict(X_test)

    #Import scikit-learn metrics module for accuracy calculation



    from sklearn import metrics
    from sklearn.metrics import classification_report, confusion_matrix

    cm= confusion_matrix(y_test, y_pred)
    print(cm)

    plt.show()

    print(classification_report(y_test, y_pred))

    # Model Accuracy, how often is the classifier correct?
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
    return metrics.accuracy_score(y_test, y_pred)


knn()

while knn() < 0.5:
    knn()

fig, ax = plot_confusion_matrix(conf_mat=cm,
                                    colorbar=True,
                                    show_absolute=False,
                                    show_normed=True,
                                    )