import pandas as pd
import librosa
import numpy as np
import json

def generate_spectrogram_data(data_path):
    sg_data = []
    audio_df = pd.read_pickle(data_path)
    
    for row in audio_df.iterrows():
        current_row = row[1]
       
        S = librosa.feature.melspectrogram(y=current_row.samples, sr=current_row.sample_rate)
        sg_data.append([S, current_row.class_label])

    df = pd.DataFrame(sg_data, columns=["data", "class_label"])
    df.to_pickle('spectrogram_data.pkl')

    print("Saved to pickle file in root directory")
    return None

generate_spectrogram_data('audio_data.pkl')