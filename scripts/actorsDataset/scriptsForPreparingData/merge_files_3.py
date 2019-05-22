import csv
import time
import json
from create_proper_JSON import *
from create_CSV_header import *


def create_list_of_ids(array_of_jsons):
    '''
    create_list_of_ids [Fuction create list of film metadata ids]

    [We use this function to create array of only ids of film_metadata ids
    and then use it when we iterate over selected dataset for merging two files in one
    It`s work like JOIN (similarly) in sql but in files]

    :param array_of_jsons: [array of jsons]
    :type array_of_jsons: [array]
    :return: [array of ids]
    :rtype: [array of strings]
    '''

    movies_metadata_Ids = []
    for iter, row in enumerate(array_of_jsons):
        filmId = row['id']
        movies_metadata_Ids.append(filmId)
    return movies_metadata_Ids


def merge_two_CSV_files_to_one():
    '''
    merge_two_CSV_files_to_one Get infromation from two files and return merged one

    [First we load two csv files 1) our prepared file 2) file with film metadate
    Next this function read files and parse it into array of JSONs
    Create output file (merged one) amd write header for this file
    Parse cells of film metadata to JSON
    Iterate over file with prepared date and selects genre, title and rating from another one, 
    store it to the variables and write to merged file
    LAso in proces of parsing we discard data which doesn`t have all filed cells]

    '''

    movies_metadata = open(
        '../../originalDataset/movies_metadata.csv', 'r', encoding="utf8")
    selected_data = open(
        '../../preparedData/outfileWithActorsAndProducer.csv', 'r', encoding="utf8")
    fout_CSV = open('../../staggingArea/mergedFile.csv', 'w', encoding="utf8")
    writer_CSV = csv.writer(fout_CSV)
    fout_JSON = open('../../staggingArea/mergedFile.json',
                     'w', encoding="utf8")

    movies_metadata_reader = csv.DictReader(movies_metadata, fieldnames=(
        "adult", "belongs_to_collection", "budget", "genres", "homepage", "id", "imdb_id", "original_language",
        "original_title", "overview", "popularity", "poster_path", "production_companies", "production_countries",
        "release_date", "revenue", "runtime", "spoken_languages", "status", "tagline", "title", "video", "vote_average",
        "vote_count"))
    selected_data_reader = csv.DictReader(selected_data, fieldnames=(
        "shit", "filmId", 'producer', 'actor'))

    # Parse the CSV into JSON
    movies_metadata_JSON = json.dumps([row for row in movies_metadata_reader])
    selected_data_JSON = json.dumps([row for row in selected_data_reader])
    movies_metadata_JSON = json.loads(movies_metadata_JSON)
    selected_data_JSON = json.loads(selected_data_JSON)

    # create and write header to csv file
    header = create_CSV_header(
        6, "filmId", "title", "genre", "producer", "actor", "rating")
    writer_CSV.writerow(header)

    # create list of IDs for better search when merge files (like JOIN)
    movies_metadata_Ids = create_list_of_ids(movies_metadata_JSON)

    print(len(movies_metadata_Ids))
    print(movies_metadata_Ids)
    # write to json file character of array start
    fout_JSON.write('[')
    for iter, object_from_selected in enumerate(selected_data_JSON):
        # ignore header of CSV
        if iter == 0:
            continue
        # get id from selected data
        filmId = object_from_selected["filmId"]
        # get position in array
        id = movies_metadata_Ids.index(filmId)
        # get film object
        movie = movies_metadata_JSON[id]
        # get all genres
        genre = create_proper_JSON(movie['genres'])
        title = movie['title']
        vote_average = movie['vote_average']
        rating = round(float(movie['vote_average']))
        # merge rating
        rating = mergeRating(rating)
        # clean from uncompleted data
        try:
            # get a main genre
            genre = json.loads(genre)[0]['name']
        except:
            print("Data isn`t  completed")
            continue
        # prepare data for writing
        producer = object_from_selected["producer"]
        actor = object_from_selected["actor"]
        row = [filmId, title, genre, producer, actor, rating]
        row_json = {"filmId": filmId, "title": title, "genre": genre,
                    "producer": producer, "actor": actor, "rating": rating}

        json.dump(row_json, fout_JSON)
        # write to json file delimiter
        fout_JSON.write(',')
        writer_CSV.writerow(row)
    # write to json file character of array end
    fout_JSON.write(']')


def mergeRating(rating):
    '''
    mergeRating [return new ranking]

    [Function return new ranikng, it means that if overage ranking 
    is less then 4 of biggest then 8
    We made it to solve classification problem]


    :param rating: [actual film rating]
    :type rating: [int]
    :return: [new rating]
    :rtype: [int]
    '''

    newRating = 0
    if rating < 4:
        newRating = 5
    elif rating > 8:
        newRating = 8
    else:
        newRating = rating
    return newRating


merge_two_CSV_files_to_one()
