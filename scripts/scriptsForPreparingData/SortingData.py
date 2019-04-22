import pandas as pd

file_name = 'mergedFile.csv'

data = pd.read_csv(file_name, sep=',')
# columns names ['filmId' 'title' 'genre' 'producer' 'actor' 'rating']

data_rating = data.groupby(['rating']).count()
print(data_rating['filmId'])

data.sort_values(by=['rating'], inplace=True)

data.to_csv('sorted.csv', index=False)


series_rating_0 = [data.iloc[i] for i in range(len(data)) if data.iloc[i]['rating'] == 0]
series_rating_2 = [data.iloc[i] for i in range(len(data)) if data.iloc[i]['rating'] == 2]
series_rating_3 = [data.iloc[i] for i in range(len(data)) if data.iloc[i]['rating'] == 3]
series_rating_4 = [data.iloc[i] for i in range(len(data)) if data.iloc[i]['rating'] == 4]
series_rating_5 = [data.iloc[i] for i in range(len(data)) if data.iloc[i]['rating'] == 5]
series_rating_6 = [data.iloc[i] for i in range(len(data)) if data.iloc[i]['rating'] == 6]
series_rating_7 = [data.iloc[i] for i in range(len(data)) if data.iloc[i]['rating'] == 7]
series_rating_8 = [data.iloc[i] for i in range(len(data)) if data.iloc[i]['rating'] == 8]
series_rating_9 = [data.iloc[i] for i in range(len(data)) if data.iloc[i]['rating'] == 9]
series_rating_10 = [data.iloc[i] for i in range(len(data)) if data.iloc[i]['rating'] == 10]

print(series_rating_0)
print(series_rating_0[0:2])
print(series_rating_0[0]['rating'])
print(type(series_rating_0))
print(type(series_rating_0[0]))


def create_popular_series(series):
    frames_part_1.append(series[0: int(len(series)/10)])
    frames_part_2.append(series[int(len(series)/10): 2*int(len(series)/10)])
    frames_part_3.append(series[2*int(len(series)/10): 3*int(len(series)/10)])
    frames_part_4.append(series[3*int(len(series)/10): 4*int(len(series)/10)])
    frames_part_5.append(series[4*int(len(series)/10): 5*int(len(series)/10)])
    frames_part_6.append(series[5*int(len(series)/10): 6*int(len(series)/10)])
    frames_part_7.append(series[6*int(len(series)/10): 7*int(len(series)/10)])
    frames_part_8.append(series[7*int(len(series)/10): 8*int(len(series)/10)])
    frames_part_9.append(series[8*int(len(series)/10): 9*int(len(series)/10)])
    frames_part_10.append(series[9*int(len(series)/10): 10*int(len(series)/10)])


# create series_rating_0
frames_part_1 = series_rating_0[0: int(len(series_rating_0)/10)]
frames_part_2 = series_rating_0[int(len(series_rating_0)/10): 2*int(len(series_rating_0)/10)]
frames_part_3 = series_rating_0[2*int(len(series_rating_0)/10): 3*int(len(series_rating_0)/10)]
frames_part_4 = series_rating_0[3*int(len(series_rating_0)/10): 4*int(len(series_rating_0)/10)]
frames_part_5 = series_rating_0[4*int(len(series_rating_0)/10): 5*int(len(series_rating_0)/10)]
frames_part_6 = series_rating_0[5*int(len(series_rating_0)/10): 6*int(len(series_rating_0)/10)]
frames_part_7 = series_rating_0[6*int(len(series_rating_0)/10): 7*int(len(series_rating_0)/10)]
frames_part_8 = series_rating_0[7*int(len(series_rating_0)/10): 8*int(len(series_rating_0)/10)]
frames_part_9 = series_rating_0[8*int(len(series_rating_0)/10): 9*int(len(series_rating_0)/10)]
frames_part_10 = series_rating_0[9*int(len(series_rating_0)/10): 10*int(len(series_rating_0)/10)]

# create another series_rating
create_popular_series(series_rating_4)
create_popular_series(series_rating_5)
create_popular_series(series_rating_6)
create_popular_series(series_rating_7)
create_popular_series(series_rating_8)


# create_extra_series

frames_part_1.append(series_rating_3[0])
frames_part_2.append(series_rating_3[1])
frames_part_3.append(series_rating_3[2])
frames_part_4.append(series_rating_3[3])
frames_part_5.append(series_rating_3[4])
frames_part_6.append(series_rating_3[5])
frames_part_7.append(series_rating_3[6])
frames_part_8.append(series_rating_3[7])

frames_part_1.append(series_rating_9[0])
frames_part_2.append(series_rating_9[1])
frames_part_3.append(series_rating_9[2])
frames_part_4.append(series_rating_9[3])

frames_part_5.append(series_rating_10[0])
frames_part_6.append(series_rating_10[1])

frames_part_7.append(series_rating_2)

frames_part_8.append(series_rating_4[0])
frames_part_9.append(series_rating_4[1:3])
frames_part_10.append(series_rating_4[3:5])


# singles series
frames_part_1.append(series_rating_5[10*int(len(series_rating_5)/10):(10*int(len(series_rating_5)/10)+2)])
frames_part_2.append(series_rating_5[(10*int(len(series_rating_5)/10)+2):(10*int(len(series_rating_5)/10)+4)])
frames_part_3.append(series_rating_5[(10*int(len(series_rating_5)/10)+4): (10*int(len(series_rating_5)/10)+6)])
frames_part_4.append(series_rating_5[(10*int(len(series_rating_5)/10)+6):])

frames_part_4.append(series_rating_6[10*int(len(series_rating_6)/10):(10*int(len(series_rating_6)/10)+1)])
frames_part_5.append(series_rating_6[(10*int(len(series_rating_6)/10)+1):(10*int(len(series_rating_6)/10)+3)])
frames_part_6.append(series_rating_6[(10*int(len(series_rating_6)/10)+3):(10*int(len(series_rating_6)/10)+5)])

frames_part_6.append(series_rating_7[(10*int(len(series_rating_7)/10)):(10*int(len(series_rating_7)/10)+1)])
frames_part_7.append(series_rating_7[(10*int(len(series_rating_7)/10)+1):(10*int(len(series_rating_7)/10)+3)])
frames_part_8.append(series_rating_7[(10*int(len(series_rating_7)/10)+3):(10*int(len(series_rating_7)/10)+5)])

frames_part_8.append(series_rating_8[(10*int(len(series_rating_8)/10)):(10*int(len(series_rating_8)/10)+1)])
frames_part_9.append(series_rating_8[(10*int(len(series_rating_8)/10)+1):(10*int(len(series_rating_8)/10)+3)])
frames_part_10.append(series_rating_8[(10*int(len(series_rating_8)/10)+3):(10*int(len(series_rating_8)/10)+4)])



def create_dataframes(frames):
    df = pd.DataFrame()
    for idx, value in enumerate(frames):
        if isinstance(value, list):
            df_x = [i for i in frames[idx]]
            df = df.append(df_x, ignore_index=True)
        else:
            df_x = pd.Series(frames[idx])
            df = df.append(df_x, ignore_index=True)

    return df

# create dataframes
df_1 = create_dataframes(frames_part_1)
df_2 = create_dataframes(frames_part_2)
df_3 = create_dataframes(frames_part_3)
df_4 = create_dataframes(frames_part_4)
df_5 = create_dataframes(frames_part_5)
df_6 = create_dataframes(frames_part_6)
df_7 = create_dataframes(frames_part_7)
df_8 = create_dataframes(frames_part_8)
df_9 = create_dataframes(frames_part_9)
df_10 = create_dataframes(frames_part_10)


# connecting dataframes
df_1 = df_1.append(df_2, ignore_index=True)
df_1 = df_1.append(df_3, ignore_index=True)
df_1 = df_1.append(df_4, ignore_index=True)
df_1 = df_1.append(df_5, ignore_index=True)
df_1 = df_1.append(df_6, ignore_index=True)
df_1 = df_1.append(df_7, ignore_index=True)
df_1 = df_1.append(df_8, ignore_index=True)
df_1 = df_1.append(df_9, ignore_index=True)
df_1 = df_1.append(df_10, ignore_index=True)

# save to file
df_1.to_csv('df.csv', index=False)


