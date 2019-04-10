import csv
import json
import re

default_input_file_path = '../../staggingArea/parsed_credits.csv.json'

# Uncomment when rns create_JSON_from_CSV script (data doesn`t exist)
# JSON_raw = open(default_input_file_path, 'r').readlines()
# JSON_object = json.loads(JSON_raw[0])
prepared_actors = open('../../preparedData/actors.txt', 'r').read().split('\n')
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


def return_new_row(old_row, producer_cell, actor_cell):
    """
    return_new_row Fuction return new immtable row

    [Immutability its one of the most needed filar in programing, 
    we used this function for immutability of our data it means,
     create new data and return it, rather then reasign variables, 
     what can be a source of bugs and perfomence issues]

    :param old_row: [old row from dataset]
    :type old_row: [array]
    :param producer_cell: [cell with producer name]
    :type producer_cell: [String]
    :param actor_cell: [cell with actor name]
    :type actor_cell: [String]
    :return: [new immutable row]
    :rtype: [Array]
    """

    # init array
    new_row = [None] * 4
    film_id = old_row[2]
    new_row[0] = old_row[0]
    new_row[1] = film_id
    new_row[2] = producer_cell
    new_row[3] = actor_cell

    return new_row


def create_proper_JSON(bad_formated_cell):
    '''
    create_proper_JSON This function create proper JSON from bad formated string
    
    [In our dataset data called "JSON" wasn`t really javascript notation object, we can call it "bad JSON" or badly fomated,
    for futher use of our dataset we was needed to transofm from "bad JSON" to array of properly formated String aka "raw JSON"]
    
    :param bad_formated_cell: [cell with bad formated data]
    :type bad_formated_cell: [String]
    :return: [properly formated String]
    :rtype: [String]
    '''

    open_brackets_replaced = bad_formated_cell.replace("{\'", "{\"")
    close_brackets_replaced = open_brackets_replaced.replace("\'}", "\"}")
    space_plus_sinqle_quote_replaced = close_brackets_replaced.replace(
        " \'", " \"")
    a3 = space_plus_sinqle_quote_replaced.replace("\',", "\",")
    single_quote_replaced = a3.replace("':", "\":")
    quote_replaced = single_quote_replaced.replace('\'', ' ')
    cell_with_proper_JSON = quote_replaced.replace("None", "1")

    return cell_with_proper_JSON


def create_CSV_header(number_of_columns, *args):
    '''
    create_CSV_header creates header for CSV file

    Using this function we can create CSV header with custom number of cols and names

    :param number_of_columns: define number of columns in row 
    :type number_of_columns: [int]
    :return: [Array of columns]
    :rtype: [Array of Strings]
    '''

    CSV_header = [None] * number_of_columns
    for id, column_name in enumerate(args):
        CSV_header[id] = column_name

    return CSV_header


def check_actor_in_film_CSV():
    '''
    check_actor_in_film_CSV Check if actor from prepared list is in a dataset

    Create output file and write custom header
    Check if actor from prepared list is in a dataset, next
    Run function for proper modifing "badJSON", after parse JSON
    In the next step function using regexp takes from field Producer name and store it.
    The main last step its create new row with needed for use data and write to a file
    Print count of films with our actor
    Print count of unique actors

    '''

    actors_in_a_films = []
    unique_actors = []
    iteration = 0
    # init output file
    fout = open('../..//helpers/outfile.csv', 'w', encoding="utf8")
    with open('../../originalDataset/credits.csv', 'r', encoding="utf8") as fin:
        writer = csv.writer(fout)
        # create and write header to csv file
        header = create_CSV_header(4, "shit", "filmId", "producer", "actor")
        writer.writerow(header)
        for row in csv.reader(fin):
            for actor in prepared_actors:
                if actor in row[0]:
                    try:
                        # assign for better readability
                        actor_cell = actor
                        # modify "bad JSON" from CSV for proper parsing
                        properly_modified_to_JSON_cell = create_proper_JSON(
                            row[1])
                        # parse to JSON
                        array_of_JSON = json.loads(
                            properly_modified_to_JSON_cell)
                        for single_object in array_of_JSON:
                            if re.search("^Producer$", single_object['job']):
                                # assign for better readability
                                producer_cell = single_object['name']
                                actors_in_a_films.append(actor)
                                new_row = return_new_row(
                                    row, producer_cell, actor_cell)
                                writer.writerow(new_row)
                                iteration += 1
                                print(iteration, producer_cell, actor_cell)
                                if actor not in unique_actors:
                                    unique_actors.append(actor)
                                break
                    except:
                        print("Problem found in parsing array of JSONS")
    print('Actors from prepared list in dataset:', len(actors_in_a_films))
    print('Unique actors count:', len(unique_actors))


check_actor_in_film_CSV()
# check_actor_infilm_JSON()
