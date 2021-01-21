def split_date(input_data):
    date = input_data.split('-')
    # return month, year 
    return int(date[0]), int(date[1])
