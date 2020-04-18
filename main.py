import pandas as pd
from build_meta import build_meta

directory = 'C:\\Users\\aming\\Desktop\\crynet\\datasets\\donateacry_corpus_cleaned_and_updated_data'
col_names = ["file_name", "full_path", "class_label"]

df = build_meta(directory, col_names)
print(df.head)