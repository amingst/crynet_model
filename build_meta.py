import pandas as pd
import os

#TODO: Change full_path to just be data dir + subdir + filename
def build_meta(directory, col_names):
    data = []
    for folder_name in os.listdir(directory):
        sub_dir = directory + "\\" + folder_name
        for file_name in os.listdir(sub_dir):
            full_path = sub_dir + "\\" + file_name
            data.append([file_name, full_path, folder_name])
    
    df = pd.DataFrame(data, columns=col_names)
    return df