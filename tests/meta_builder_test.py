import pandas as pd
import os

def build_meta(directory, col_names):
    data = []
    for folder_name in os.listdir(directory):
        sub_dir = directory + "\\" + folder_name
        for file_name in os.listdir(sub_dir):
            full_path = sub_dir + "\\" + file_name
            data.append([file_name, full_path, folder_name])
    
    df = pd.DataFrame(data, columns=col_names)
    
    df.to_csv('meta.csv', index=False)    
    print("Generated metadata file in root directory")

    return None

#TODO: Use os.path.join to dynamically use directory
directory = 'C:\\Users\\aming\\Desktop\\crynet\\datasets\\donateacry_corpus_cleaned_and_updated_data'
col_names = ["file_name", "full_path", "class_label"]

build_meta(directory, col_names)