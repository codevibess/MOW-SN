import pandas as pd
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn import preprocessing


def create_grid_search():
    data = pd.read_csv('df.csv', sep=',')

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

    parameters = [{'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000], 'kernel': ['rbf'],
                   'gamma': [0.001, 0.01, 0.1, 1, 10, 100, 1000]}]

    # parameters = [{'C': [0.6, 0.7, 0.8, 0.9, 1.1, 1.3, 1.5, 1.7, 1.9], 'kernel': ['rbf'],
    #                'gamma': [5.9, 7.8, 8.8, 9.5, 10.8, 11.9, 13.9, 15.3]}]

    grid_search = GridSearchCV(estimator=classifier, param_grid=parameters, scoring='accuracy', cv=10, n_jobs=-1)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)

    grid_search = grid_search.fit(X_train, y_train)
    best_accuracy = grid_search.best_score_
    best_parameters = grid_search.best_params_
    print('Best accuracy -> ', best_accuracy)
    print('Best parameters -> ', best_parameters)


if __name__ == '__main__':
    create_grid_search()
