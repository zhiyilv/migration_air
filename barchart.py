import os
import pickle
import csv


folder = 'D:\\weibo'
file_list = os.listdir(folder)
c_list = [i for i in file_list if i.endswith('.csv') and i.startswith('week')]
e_list = [i for i in file_list if i.endswith('extracted')]
r_list = [i for i in file_list if i.endswith('refined')]

total_count = [0]*52
for c in c_list:
    with open(os.path.join(folder, c), encoding='utf-8', errors='replace') as c_ref:
        myreader = csv.reader(c_ref)
        line_count = 0
        for i in myreader:
            line_count += 1

        line_count -= 1  # exclude the header
        week_num = int(c[4:-4])
        total_count[week_num-1] = line_count
        print('there are totally {} weibo in {}'.format(line_count, c))

geo_count = [0]*52
for e in e_list:
    with open(os.path.join(folder, e), 'rb') as e_ref:
        extracted_raw = pickle.load(e_ref)
    week_num = int(e[4:-14])
    geo_count[week_num-1] = len(extracted_raw) - 1
    print('there are totally {} geo_tagged weibo in week {}'.format(len(extracted_raw)-1, week_num))

valid_count = [0]*52
for r in r_list:
    with open(os.path.join(folder, r), 'rb') as r_ref:
        extracted_valid = pickle.load(r_ref)
    week_num = int(r[4:-12])
    valid_count[week_num-1] = len(extracted_valid) - 1
    print('there are totally {} valid tagged weibo in week {}'.format(len(extracted_valid)-1, week_num))

file_to_write = 'counts.pickle'
with open(os.path.join(folder, file_to_write), 'wb') as p_ref:
    pickle.dump([total_count, geo_count, valid_count], p_ref)
    print('these three counts are written in {}'.format(file_to_write))



