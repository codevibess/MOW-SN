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