import pandas as pd
import numpy as np
import librosa

#TODO: Figure out why param n_mfcc doesn't work
def generate_mfcc_data(data_path):
    mfcc_data = []
    audio_df = pd.read_pickle(data_path)

    for row in audio_df.iterrows():
        current_row = row[1]

        mfccs = librosa.feature.melspectrogram(y=current_row.samples, sr=current_row.sample_rate, S=None)
        scaled_mfccs = np.mean(mfccs.T, axis=0)

        mfcc_data.append([mfccs, scaled_mfccs, current_row.sample_rate, current_row.class_label])
    
    df = pd.DataFrame(mfcc_data, columns=["mfccs", "scaled_mfccs", "sr", "class_label"])
    df.to_pickle('mfcc_data.pkl')

    print("Saved to pickle file in root directory")
    return None

