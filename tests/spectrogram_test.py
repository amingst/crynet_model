import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
f_name = 'test.wav'
samples, sample_rate = librosa.load(f_name)

fig = plt.figure(figsize=[4, 4])
ax = fig.add_subplot(111)
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)
ax.set_frame_on(False)
S = librosa.feature.melspectrogram(y=samples, sr=sample_rate)
librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
plt.show()
