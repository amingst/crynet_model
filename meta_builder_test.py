import pandas as pd
from build_meta import build_meta

#TODO: Use os.path.join to dynamically use directory
directory = 'C:\\Users\\aming\\Desktop\\crynet\\datasets\\donateacry_corpus_cleaned_and_updated_data'
col_names = ["file_name", "full_path", "class_label"]

build_meta(directory, col_names)

#df.to_csv('meta.csv', index=False)