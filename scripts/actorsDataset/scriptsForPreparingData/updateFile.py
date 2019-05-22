import csv
import time
import json
from create_proper_JSON import *
from create_CSV_header import *


def merge_two_CSV_files_to_one():
    

    
    fin = open(
        '../../preparedData/df.csv', 'r', encoding="utf8")
    fout_CSV = open('../../staggingArea/updatedFile.csv', 'w', encoding="utf8")
    writer_CSV = csv.writer(fout_CSV)

    fin_reader = csv.DictReader(fin, fieldnames=(
        "actor", "filmId",  "genre", "producer", "rating", "title"))

    # Parse the CSV into JSON
    fin_JSON = json.dumps([row for row in fin_reader])

    fin_DICT = json.loads(fin_JSON)

    for iter, object_from_selected in enumerate(fin_DICT):
        # ignore header of CSV
        if iter == 0:
            continue
        print(object_from_selected)
        filmId = object_from_selected["filmId"]
        filmId = int(float(object_from_selected["filmId"]))
        # get all genres
        genre = object_from_selected['genre']
        title = object_from_selected['title']

        rating = object_from_selected['rating']
        # merge rating
        rating = mergeRating(rating)
        # clean from uncompleted data

        # prepare data for writing
        producer = object_from_selected["producer"]
        actor = object_from_selected["actor"]
        row = [actor, filmId, genre, producer, rating, title]

        writer_CSV.writerow(row)


def mergeRating(rating):
    '''
    mergeRating [return new ranking]

    [Fynction return new ranikng, it means that if overage ranking
    is less then 4 of biggest then 8
    We made it to solve classification problem]


    :param rating: [actual film rating]
    :type rating: [int]
    :return: [new rating]
    :rtype: [int]
    '''

    newRating = 0

    oldRating = int(float(rating))

    if oldRating < 5:
        newRating = 5
    elif oldRating > 8:
        newRating = 8
    else:
        newRating = oldRating
    return newRating


merge_two_CSV_files_to_one()
