from sklearn.model_selection import KFold, cross_val_score
from sklearn import linear_model
import pandas as pd
import os
import shutil

file_name = 'df.csv'

data = pd.read_csv(file_name, sep=',')
# columns names ['filmId' 'title' 'genre' 'producer' 'actor' 'rating']

data_rating = data.groupby(['rating']).count()
print(data_rating['filmId'])

kf = KFold(n_splits=10)
index_for_cv = data.index.values.tolist()
kf.get_n_splits(index_for_cv)

list_of_all_indexes = []
lasso = linear_model.Lasso()

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

print(len(list_of_all_indexes))
print(len(list_of_all_indexes[0]))


# removing directory on name CV with all files
if os.path.exists('CV'):
    shutil.rmtree('CV', ignore_errors=True)

# creating new empty directory on name CV
if not os.path.exists('CV'):
    os.mkdir('CV')

for cv_step in range(len(list_of_all_indexes)):
    df_train = pd.DataFrame()
    df_test = pd.DataFrame()
    for kind_data in range(len(list_of_all_indexes[cv_step])):
        for single_row in range(len(list_of_all_indexes[cv_step][kind_data])):
            if kind_data == 0:
                index_to_print = list_of_all_indexes[cv_step][kind_data][single_row]
                df_x = pd.Series(data.loc[index_to_print])
                df_train = df_train.append(df_x, ignore_index=True)
            else:
                index_to_print = list_of_all_indexes[cv_step][kind_data][single_row]
                df_x = pd.Series(data.loc[index_to_print])
                df_test = df_test.append(df_x, ignore_index=True)
                
    # saving  files in specific path and name
    df_train.to_csv('CV/train' + str(cv_step+1) + '.csv', index=False)
    df_test.to_csv('CV/test' + str(cv_step+1) + '.csv', index=False)
