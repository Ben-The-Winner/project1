import time
import librosa
from tkinter import *
import pymongo
from playsound import playsound
from songify import songify



#move from here 
def convert_to_dict(lst):
    res_dct = {str(i): lst[i] for i in range(0, len(lst), 1)}
    return res_dct

def tone_fix(notes):
    fix_notes=[]
    for i in notes:
        x=librosa.note_to_midi(i)
        x=x+1
        i=librosa.midi_to_note(x)
        fix_notes.append(i)
    return fix_notes




def identify_notes(y):
    D_short = librosa.stft(y)
    result = librosa.hz_to_note(D_short[1])
    return result


def load_file(filename):
    client = pymongo.MongoClient("mongodb+srv://ben6119070:BL246810@cluster0.qojmx.mongodb.net/OnABetterNote?retryWrites=true&w=majority")
    dbcol = client["OnABetterNote"]["Notes"]
    result = {}

    # 2. Load the audio as a waveform `y`, Store the sampling rate as `sr`
    y, sr = librosa.load(filename, duration= 1.5)

    # 3. Extract the notes 
    notes= identify_notes(y)
    print(notes)
    result["original_notes"] = notes
    res=convert_to_dict(notes)
    dbrecords={}
    dbrecords['res']=res
    dbrecords['ts']=time.time()
    dbcol.insert_one(dbrecords)
    # 4. Rearrange them with an algo from songify.py
    s_notes = songify(dbcol)
    print(s_notes)
    result["shuffled_notes"] = s_notes

    # 5. Run the default beat tracker
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    result["tempo"] = tempo

    # 6. Convert the frame indices of beat events into timestamps
    result["beat_times"] = librosa.frames_to_time(beat_frames,sr=sr)
    return result



def custom_play_notes(notes_list):
    #recieving  list of notes and play them with custom sound
    playsound("damusic-master/note_sounds/Beatbox.wav", block=False)
    for i in notes_list:
       try:
           if i[1]=="♯":
                playsound("damusic-master/note_sounds/"+i[0]+i[1]+"-1.wav", block=True)
           else:
                playsound("damusic-master/note_sounds/"+i[0]+"-1.wav", block=True)
       except:
          print("file not found could not play note: "+ i)
            
    return
