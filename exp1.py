import os
import csv
import pandas as pd


data_folder = "D:\weibo"

file_list = [i for i in os.listdir(data_folder) if i.endswith('.csv')]


f1 = os.path.join(data_folder, file_list[0])
# chunksize = 100
# tag = 0
# for c in pd.read_csv(f1, chunksize=chunksize):
#     if tag > 0:
#         pass
#     else:
#         print(c)

# with open(f1, encoding='utf-8', errors='replace') as f:
#     myreader = csv.reader(f)
#     flag = 0
#     line_count = 0
#     for line in myreader:
#         line_count += 1
#         if flag > 100:
#             break
#         elif line[7] != '':
#             # print(line[-5])
#             print('line: {}, info: {}'.format(line_count, line[7:]))
#             flag += 1

store = []
with open(f1, encoding='utf-8') as f:
    myreader = csv.reader(f)
    line_count = 0


