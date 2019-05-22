import pandas as pd
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn import preprocessing


def create_grid_search():
    data = pd.read_csv('../../preparedData/updatedFile.csv', sep=',')

    titles = data['title'].values
    genres = data['genre'].values
    producers = data['producer'].values
    actors = data['actor'].values
    y = data['rating'].values

    le = preprocessing.LabelEncoder()
    titles_encoded = le.fit_transform(titles)
    genres_encoded = le.fit_transform(genres)
    producers_encoded = le.fit_transform(producers)
    actors_encoded = le.fit_transform(actors)

    features = list(zip(genres_encoded, producers_encoded, actors_encoded, titles_encoded))

    scaler = StandardScaler()
    X = scaler.fit_transform(features)

    classifier = SVC(kernel='rbf')

    parameters = [{'C': [1, 10, 100, 500, 5000, 10000],
                   'kernel': ['rbf'],
                   'gamma': [1, 0.8, 0.5, 0.3, 0.1, 0.05, 0.01, 0.001]}]


    grid_search = GridSearchCV(estimator=classifier, param_grid=parameters, scoring='accuracy', cv=10, n_jobs=-1)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)

    grid_search = grid_search.fit(X_train, y_train)
    best_accuracy = grid_search.best_score_
    best_parameters = grid_search.best_params_
    print('Best accuracy -> ', best_accuracy)
    print('Best parameters -> ', best_parameters)


if __name__ == '__main__':
    create_grid_search()
