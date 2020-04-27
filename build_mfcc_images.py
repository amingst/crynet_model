import os
import librosa
import librosa.display
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from generate_img import generate_img
from save_img import save_img

# TODO: Add Completed Message
# TODO: Save image to datasets
def build_mfcc_images(data_path):
    audio_df = pd.read_pickle(data_path)
    
    for idx, row in audio_df.iterrows():
        fig = generate_img(row[0], row[1])
        img_name = str(idx) + '.png'
        save_img(fig, './img/', img_name, row[2])

    return None