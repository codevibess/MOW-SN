from sklearn.model_selection import KFold, train_test_split
import pandas as pd

file_name = '../../preparedData/mergedFile.csv'

data = pd.read_csv(file_name, sep=',')
# columns names ['filmId' 'title' 'genre' 'producer' 'actor' 'rating']

data_rating = data.groupby(['rating']).count()
print(data_rating['filmId'])

kf = KFold(n_splits=10)
index_for_cv = data.index.values.tolist()
kf.get_n_splits(index_for_cv)

list_of_all_indexes = []

for train_index, test_index in kf.split(index_for_cv):
    print("TRAIN:", train_index, "TEST:", test_index)
    list_of_indexes = []
    list_of_indexes.append(train_index)
    list_of_indexes.append(test_index)
    list_of_all_indexes.append(list_of_indexes)

# first variable cv move(1-10) from 0 to 9
# second variable kind of data (0 for train and 1 for test)
# third variable controls indexes - values of test or train data

index_to_print = list_of_all_indexes[0][1][3]
print(data['title'][index_to_print])    # print specific value
print(data.loc[index_to_print])     # print whole row


