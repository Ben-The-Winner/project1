# Beat tracking example not origin

import librosa
# import numpy as np
# import matplotlib.pyplot as plt
# import librosa.display
from songify import songify
import IPython.display as ipd
# import mir_eval.sonify

# 1. Get the file path to an included audio example
filename = librosa.example('nutcracker')
ipd.Audio(filename)
# 2. Load the audio as a waveform `y`, Store the sampling rate as `sr`
y, sr = librosa.load(filename)
playsound()
# 3. Extract the notes 
#notes = librosa.midi_to_note(range(0,22), key='F:min')
#print('original note: ', notes)

# 4. Rearrange them with an algo from songify.py
#notes = songify(notes)
#print('shuffled notes: ', notes)

# 5. Run the default beat tracker
#tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
#print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

# 4. Convert the frame indices of beat events into timestamps
#beat_times = librosa.frames_to_time(beat_frames, sr=sr)

