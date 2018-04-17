import zipfile
import os


zip_path = "D:\\weibo"
file_list = [i for i in os.listdir(zip_path) if i.endswith('zip')]

for i in file_list:
    if i != 'week1.zip':
        with zipfile.ZipFile(os.path.join(zip_path, i), 'r') as zip_ref:
            zip_ref.extractall(zip_path)



