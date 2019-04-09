import csv
import json
import re

default_input_file_path = '../../staggingArea/parsed_credits.csv.json'

#
# JSON_raw = open(default_input_file_path, 'r').readlines()
# JSON_object = json.loads(JSON_raw[0])
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


# check_actor_infilm_JSON()


fout = open('../..//helpers/outfile.csv', 'w', encoding="utf8")

def modify_CSV_by_adding_name_of_actor(row_to_modify, actor_name):
    '''
    modify_CSV_by_adding_name_of_actor Modify row from original dataset

    Modify row by a new value (actor name)

    :param row_to_modify: row number
    :type row_to_modify: String
    :param actor_name: Name of an actor
    :type actor_name: String
    :return: Modyfied row
    :rtype: String
    '''

    row_to_modify = actor_name
    return row_to_modify


test = open('./actorsInAFilms.txt', 'w')
def check_actor_in_film_CSV():
    '''
    check_actor_in_film_CSV Check if actor from prepared list is in a dataset

    
    Check if actor from prepared list is in a dataset
    Print count of films with our actor
    Print count of unique actors
    
    '''

    actors_in_a_films=[]
    unique_actors=[]
    temp=[1]
    iteration=0
    new_row=[None]*6
    with open('../../originalDataset/credits.csv', 'r', encoding="utf8") as fin:
        writer = csv.writer(fout)
        for row in csv.reader(fin):
            for actor in prepared_actors:
                if actor in row[0]:

                    try:
                        row[4] = modify_CSV_by_adding_name_of_actor(row[1], actor)
                        a0 = row[1].replace("\':,", "\":")
                        a=row[1].replace("{\'","{\"")
                        a2 =a.replace(" \'", " \"")
                        a3 = a2.replace("\',", "\",")
                        a4 = a3.replace("':", "\":")
                        a5=a4.replace("\'}","\"}")
                        a6 = a5.replace('\'', ' ')
                        b = a6.replace("None", "1")
                        # b1 = b.split(']')
                        # b2=b1[0]+"]"

                        # print(b)
                        # test.write(b2)
                        test.write(',')
                        js=json.loads(b)
                        for obj in js:
                            # if obj['job'] == 'Producer':
                            if re.search("^Producer$", obj['job']):
                                print(obj['job'], obj['name'])
                                iteration+=1
                                print(iteration)
                                temp[0]=row[1]
                                actors_in_a_films.append(actor)


                                new_row[0]=row[0]
                                new_row[1] = obj['name']
                                new_row[2] = row[2]
                                new_row[3] = row[3]
                                new_row[4] = row[4]
                                writer.writerow(new_row)
                                if actor not in unique_actors:
                                    unique_actors.append(actor)
                                break
                    except:
                        print("LOL")
    print('Actors from prepared list in dataset:', len(actors_in_a_films))
    print('Unique actors count:', len(unique_actors))





check_actor_in_film_CSV()