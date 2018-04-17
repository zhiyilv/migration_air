# check whether all starts with POINT
import pickle
import os


folder = "D:\\weibo"
refined_list = [i for i in os.listdir(folder) if i.endswith('refined')]

for r in refined_list:
    print('dealing with {}'.format(r))
    with open(os.path.join(folder, r), 'rb') as file_ref:
        r_file = pickle.load(file_ref)
    err_count = 0
    for i in r_file:
        if not i[7].startswith('POINT'):
            err_count += 1
    if err_count > 0:
        print('in file {} there are {} not endswith POINT\n'.format(r, err_count))


