import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#Importing the Dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
file ='../../preparedData/mergedFile.csv'

# Assign colum names to the dataset
# We use separator delimiter instead
# names = ['filmId', 'title', 'genre', 'producer', 'actor', 'rating']

# read dataset to pandas dataframe
dataset = pd.read_csv(file, sep=',')
print(dataset.head())

# The next step is to split our dataset into
# its attributes and labels:
X = dataset.iloc[:, :-1].values
titles = dataset.iloc[:, 1].values
genres = dataset.iloc[:, 2].values
producers = dataset.iloc[:, 3].values
actors = dataset.iloc[:, 4].values
y = dataset.iloc[:, 5].values
print(actors)


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
features=list(zip(genres_encoded,producers_encoded,actors_encoded))


# To avoid over-fitting, we will divide our dataset into training and test splits, which gives us
# a better idea as to how our algorithm performed during the testing phase.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(features, y, test_size=0.20)




from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=7)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))