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
