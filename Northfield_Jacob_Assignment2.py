# import modules:

import csv  # for reading the csv
import os  # for using the file path


# define function to read and validate file

def load_census_data(your_file):
    with open(your_file, 'r') as in_file:  # open file to be read
        reader = csv.DictReader(in_file)
        columns = reader.fieldnames  # identify the column headers for the file
        master_list = []  # create empty list to use for collection at end of function

        # loop to validate int, the keys in the rows, then the number of keys in the row

        for row in reader:
            try:
                row_translate = {str(key): int(value) for key, value in row.items()}
                for key in row_translate.items():
                    if key in columns:
                        if len(row) == 7:
                            continue
            except ValueError:
                continue  # skip rows that don't validate
            master_list.append(row_translate)

    stripped_file = (tuple(master_list))  # the new tuple of rows
    return stripped_file

# save initial results in variable

results = (load_census_data(os.path.realpath('2010_Census_Populations_by_Zip_Code.csv')))
print(results)

# filter list by column values

def filter_data_by_column_and_floor(info, columns, values):

    for row in info:
        for key, value in row.items():
            if key in columns:
                if value > values:
                    results_list.append(row)
                    continue
    filtered_results = tuple(results_list)
    return filtered_results

# identify column headers

def fields():
    column_names = []

    for row in results:
        for key in row:
            header = key
            column_names.append(header)
        break
    return column_names

column_names = fields()

# enumerate headers

def data_tags():
    # store column names in a tuple

    field_names = (tuple(column_names))

    # enumerate tuple

    tags = list(enumerate(field_names, start=1))
    return tags

# get user input for integer with three reattempts

def input_for_validation(question):
    user_attempts = 0
    while user_attempts < 4:
        user_column = input(question)
        try:
            user_number = int(user_column)
            if user_number - 1  < data_tags().index(min(data_tags())):
                print('That number is too low for the list.')
                user_attempts += 1
            elif user_number - 1 > data_tags().index(max(data_tags())):
                print('That number is too high for the list.')
                user_attempts += 1
            else:
                return int(user_number) - 1
        except ValueError:
            print('That is not an option.')
            user_attempts += 1
        if user_attempts > 3:
            print("You're bad at this.")
            exit()

# get user input for floor

def input_for_filter():
    user_attempts_two = 0
    while user_attempts_two < 4:
        user = input("What data would you like to filter by?")
        try:
            user_number = int(user)
            if user_number < 1:
                print('That number is too low for the list.')
                user_attempts_two += 1
            else:
                return user_number
        except ValueError:
            print('That is not a positive number.')
            user_attempts_two += 1
        if user_attempts_two > 3:
            print("You're bad at this.")
            exit()

    user_filter = input_for_filter()
    return user_filter

# begin by showing the user headers

print(*data_tags(), sep='\n')
user_column = input_for_validation("Which column would you like to filter by?")
user_filter_output = input_for_filter()
user_column_output = (data_tags()[user_column][1])
user_column_sort = input_for_validation("Which column would you like to sort by?")
user_column_sort_output = (data_tags()[user_column_sort][1])
results_list = []

rows_to_sort = filter_data_by_column_and_floor(results, user_column_output, user_filter_output)

# sort filtered list

sorted_results = (sorted(rows_to_sort, key=lambda data_tags: data_tags[user_column_sort_output]))

# save new sorted list to a new file in export folder

def save():
    if not os.path.isdir('export'):
        os.makedirs('export')
    attempts = 0

    while attempts < 4:
        user = input("Please select a unique name for your file.")
        if user:
            name = user + '.csv'
            way_to_file = os.path.join('export', name) # create file path
            if not os.path.isfile(way_to_file): # check for file path
                with open((way_to_file), 'w') as in_file:  # open file to be written
                    writer = csv.DictWriter(in_file, column_names)
                    writer.writeheader() # write header
                    for row in sorted_results:
                        writer.writerow(row) # write rows
                exit()
            elif os.path.isfile(way_to_file):
                attempts += 1
        else:
            attempts += 1
    return


save()

if __name__ == '__main__':
    main()

