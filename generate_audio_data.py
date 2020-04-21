import pandas as pd
import librosa
import numpy as np

def generate_audio_data(meta_path):
    audio_data = []
    meta_df = pd.read_csv(meta_path)

    for row in meta_df.iterrows():
        current_row = row[1]
        
        samples, sample_rate = librosa.load(current_row[1])
        audio_data.append([samples, sample_rate, current_row[2]])

    df = pd.DataFrame(audio_data, columns=["samples", "sample_rate", "class_label"])
    df.to_pickle('audio_data.pkl')

    print("Saved to pickle file in root directory")
    return None