import csv
import json


default_input_file_path = '../../staggingArea/parsed_credits.csv.json'


JSON_raw = open(default_input_file_path, 'r').readlines()
JSON_object = json.loads(JSON_raw[0])
prepared_actors = open('../../actors', 'r').read().split('\n')
actorsInAFilms = open('./actorsInAFilms.txt', 'w')


def check_actor_infilm_JSON():
    '''
    check_actor_infilm_JSON Check if actor from prepared list is in a dataset

    Check if actor from prepared list is in a dataset
    Print count of films with our actor
    Print count of unique actors

    '''

    actors_in_a_films = []
    unique_actors = []
    for single_object in JSON_object:
        for actor in prepared_actors:
            if actor in single_object["cast"]:
                actors_in_a_films.append(actor)
                if actor not in unique_actors:
                    unique_actors.append(actor)

    print('Actors from prepared list in dataset:', len(actors_in_a_films))
    print('Unique actors count:', len(unique_actors))


check_actor_infilm_JSON()


# fout = open('./outfile.csv', 'w', encoding="utf8")
#
# with open('../originalDataset/credits.csv', 'r', encoding="utf8") as fin:
#     writer = csv.writer(fout)
#     for row in csv.reader(fin):
#         iteration += 1
#         for actor in lines:
#             if actor in row[0]:
#                 row[1] = actor
#
#                 actorsInAFilmsArray.append(actor)
#                 filmArray.append(row[2])
#                 writer.write(row)
#
#
# for word in actorsInAFilmsArray:
#     if word not in actorsInAFilmsArrayFinal:
#         actorsInAFilmsArrayFinal.append(word)
#
# for word in filmArray:
#     if word not in films:
#         films.append(word)
