# Beat tracking example

import librosa
from tkinter import *
from pandas import array
import pymongo
from playsound import playsound
from songify import songify
import IPython.display as ipd
import numpy as np
import soundfile as sf

root = Tk()
root.geometry("800x800")

title=Label(root,text="On a Better Note",bd=9,relief=GROOVE,
font=("times new roman",50,"bold"),bg="green",fg="yellow")
title.pack(side=TOP,fill=X)

input= Entry(root, width=100)
input.pack()
input.insert(0,"enter file or press an option button: ")


def play():
    playsound(input.get(), block= False)
    
def play3_wav():
    playsound("the_song_files/sample3.wav",block=False)
    
def stop():
    stop()       
    

 
# making a button which trigger the function so sound can be played
play_button = Button(root, text="Play the song you entered", font=("Helvetica", 20),
relief=GROOVE, command=play,bg="green")
play_button.pack(pady=20)

stop_button = Button(root, text="Stop", font=("Helvetica", 15),
relief=GROOVE, command=stop,bg="green")
stop_button.pack(pady=20)


play_sample3_wav = Button(root, text="Play sample3.wav", font=("Helvetica", 10),
relief=GROOVE, command=play3_wav,bg="green")
play_sample3_wav.pack(pady=20)


def convert(lst):
    res_dct = {str(i): lst[i] for i in range(0, len(lst), 1)}
    return res_dct

def load_file(filename):
    client = pymongo.MongoClient("mongodb+srv://ben6119070:BL246810@cluster0.qojmx.mongodb.net/OnABetterNote?retryWrites=true&w=majority")
    dbcol= client["OnABetterNote"]["Notes"]
    result = {}
    # 2. Load the audio as a waveform `y`, Store the sampling rate as `sr`
    y, sr = librosa.load(filename)

    # 3. Extract the notes 
    notes = librosa.midi_to_note(range(0,12), key='B:min')
    result["original_notes"] = notes
    sf.write('stereo_file.wav', y, 44100, 'PCM_24')
    res=convert(notes)
    dbcol.insert_one(res)
    # 4. Rearrange them with an algo from songify.py
    s_notes = songify(dbcol)
    result["shuffled_notes"] = s_notes

    # 5. Run the default beat tracker
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    result["tempo"] = tempo

    # 6. Convert the frame indices of beat events into timestamps
    result["beat_times"] = librosa.frames_to_time(beat_frames, sr=sr)
    return result



def custom_play_notes(notes_list):
    #recieving  list of notes and play them with custom sound
    for i in notes_list:
        print("note " +i+" is ")
        try:
            playsound("note_sounds/"+i+".wav", block=False)
        except:
            print("file not found could not play note: "+ i)
            
    return


# 1. Get the file path to an included audio example
filename = "stereo_file.wav"
result = load_file(filename)




def click_display_original_notes():
    myLabel = Label(root, text = result["original_notes"])
    myLabel.pack()

def click_play_shuffled_notes():
    myLabel2 = Label(root, text = result["shuffled_notes"])
    myLabel2.pack()
    custom_play_notes(result["shuffled_notes"])

def click_display_tempo():
    myLabel3 = Label(root, text = result["tempo"])
    myLabel3.pack()



myButton= Button(root, text= "click here to see the original notes", command= click_display_original_notes, bg="green")
myButton.pack()

myButton2= Button(root, text= "click here to see the shuffled notes", command= click_play_shuffled_notes, bg="green")
myButton2.pack()

myButton3= Button(root, text= "click here to see the tempo", command= click_display_tempo, bg="green")
myButton3.pack()

root.configure(background="yellow")


root.mainloop()


