import csv
import time
import json
from create_proper_JSON import *
from create_CSV_header import *


def merge_two_CSV_files_to_one():

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
    movies_metadata_Ids = []

    # create and write header to csv file
    header = create_CSV_header(6, "filmId", "title", "genre", "producer", "actor", "rating")
    writer_CSV.writerow(header)

    for iter, row in enumerate(movies_metadata_JSON):
        filmId = row['id']
        movies_metadata_Ids.append(filmId)

    print(len(movies_metadata_Ids))
    print(movies_metadata_Ids)

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
        fout_JSON.write(',')
        writer_CSV.writerow(row)
    fout_JSON.write(']')

merge_two_CSV_files_to_one()
