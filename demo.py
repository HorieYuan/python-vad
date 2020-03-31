import librosa
import numpy as np

from pyvad import split

path = "vocals.wav"
x, sr = librosa.load(path)
edges = split(x, sr, vad_mode=3)
y = []
for edge in edges:
    y.append(x[edge[0]:edge[1]])
y = np.concatenate(y)
librosa.output.write_wav(p + "pure_vocal.wav", y, sr)
