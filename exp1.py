# from csv files, extract those geo-tagged lines
import os
import csv
import pandas as pd
import pickle


data_folder = "D:\weibo"

file_list = [i for i in os.listdir(data_folder) if i.endswith('.csv') and i.startswith('week')]

# f1 = os.path.join(data_folder, file_list[0])
# store = []
# with open(f1, encoding='utf-8', errors='replace') as f:
#     myreader = csv.reader(f)
#     line_count = 0
#     extract_count = 0
#     for line in myreader:
#         line_count += 1
#         if line[7]:
#             extract_count += 1
#             store.append(line)
#             print('line: {}, no.: {}, info: {}'.format(line_count, extract_count, line[7:]))

for file_name in file_list:
    store = []
    line_count = 0
    with open(os.path.join(data_folder, file_name), encoding='utf-8', errors='replace') as ref:
        myreader = csv.reader(ref)
        print('dealing with file {}'.format(file_name))
        for line in myreader:
            line_count += 1
            if line[7]:
                store.append(line)
    print('extracted {} geo-tagged weibo from {} in total'.format(len(store), line_count))

    # store
    with open(os.path.join(data_folder, '{}_extracted'.format(file_name)), 'wb') as p_file:
        pickle.dump(store, p_file)
    print('stored in {}_extracted\n'.format(file_name))


