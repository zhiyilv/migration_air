# from extracted files, exclude those lines with POINT(0 0)
import pickle
import os


folder = "D:\\weibo"
file_list = [i for i in os.listdir(folder) if i.endswith('extracted')]

# f1 = os.path.join(folder, file_list[0])
# with open(f1, 'rb') as fref:
#     ff = pickle.load(fref)
#
# count = 0
# for line in ff:
#     if line[7] == 'POINT(0 0)':
#         count += 1


for file_name in file_list:
    refined = []
    print('dealing with file {}'.format(file_name))
    with open(os.path.join(folder, file_name), 'rb') as file_ref:
        file_raw = pickle.load(file_ref)

    # note tha the header is included in raw file
    refined = [i for i in file_raw[1:] if i[7] != 'POINT(0 0)']
    print('excluded {} POINT(0 0)'.format(len(file_raw) - len(refined) - 1))

    new_name = '{}refined'.format(file_name[:-9])
    with open(os.path.join(folder, new_name), 'wb') as p_file:
        pickle.dump(refined, p_file)
    print('stored in {}\n'.format(new_name))



