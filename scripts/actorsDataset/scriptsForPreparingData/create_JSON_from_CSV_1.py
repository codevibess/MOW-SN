import csv
import json
import sys

default_input_file_path = '../../originalDataset/credits.csv'
default_input_file = default_input_file_path.split("/")[-1]
default_outfile_file_path = '../../staggingArea/parsed_' + \
    default_input_file + '.json'


def parse_CSV_to_JSON(input_file=default_input_file_path, outfile_file=default_outfile_file_path):
    '''
    parse_CSV_to_JSON Parse CSV File to JSON Object

    This function open specified csv file (first argument)
    Next read file and store all data in memory
    The next step its parsing from CSB to JSON
    and save output to file which was specified as a second parameter of a function

    :param input_file: csv input file 
    :type input_file: String
    :param outfile_file: json output file
    :type outfile_file: String
    :return: JSON object of parsed CSV
    :rtype: JSON
    '''

    # Open the CSV
    csv_file = open(input_file, encoding="utf8")

    # Change each fieldname to the appropriate field name.
    reader = csv.DictReader(csv_file, fieldnames=("cast", "crew", "id"))

    #  Parse the CSV into JSON
    json_object = json.dumps([row for row in reader])
    print("JSON parsed!")

    # Save the JSON
    json_file = open(outfile_file, 'w')
    json_file.write(json_object)
    print("JSON Saved to file!")
    return json_object


if len(sys.argv) > 3:
    parse_CSV_to_JSON(sys.argv[1], sys.argv[2])
else:
    parse_CSV_to_JSON()
