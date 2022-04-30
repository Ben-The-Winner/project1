# Beat tracking example

import librosa
from tkinter import *
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
    
def play1():
    playsound("sample1 (copy).wav", block=False)

def play2():
    playsound("sample3.wav",block=False)

def play3():
    playsound("stereo_file.wav",block=False)
    
def stop():
    stop()       
    


 
# making a button which trigger the function so sound can be played
play_button = Button(root, text="Play the song you entered", font=("Helvetica", 20),
relief=GROOVE, command=play,bg="green")
play_button.pack(pady=20)

stop_button = Button(root, text="Stop", font=("Helvetica", 15),
relief=GROOVE, command=stop,bg="green")
stop_button.pack(pady=20)

play_button1 = Button(root, text="Play Option1: sample1 (copy).wav", font=("Helvetica", 10),
relief=GROOVE, command=play1,bg="green")
play_button1.pack(pady=20)

play_button2 = Button(root, text="Play Option2: sample3.wav", font=("Helvetica", 10),
relief=GROOVE, command=play2,bg="green")
play_button2.pack(pady=20)

play_button3 = Button(root, text="Play Option3: stereo_file.wav", font=("Helvetica", 10),
relief=GROOVE, command=play3,bg="green")
play_button3.pack(pady=20)


def convert(lst):
    res_dct = {str(i): lst[i] for i in range(0, len(lst), 1)}
    return res_dct






def custom_play_notes(notes_list):
    #recieving  list of notes and play them with custom sound
    for i in notes_list:
        print("note " +i+" is ")
        try:
            playsound("note_sounds/"+i+".wav", block=False)
        except:
            print("file not found could not play note: "+ i)
            
    return

client = pymongo.MongoClient("mongodb+srv://ben6119070:BL246810@cluster0.qojmx.mongodb.net/OnABetterNote?retryWrites=true&w=majority")
dbcol= client["OnABetterNote"]["Notes"]


# 1. Get the file path to an included audio example
filename = librosa.example('nutcracker')
ipd.Audio(filename)
# 2. Load the audio as a waveform `y`, Store the sampling rate as `sr`
y, sr = librosa.load(filename)


# 3. Extract the notes 
notes = librosa.midi_to_note(range(0,12), key='B:min')
words = notes
sf.write('stereo_file.wav', y, 44100, 'PCM_24')
res=convert(notes)
#custom_play_notes(res)
dbcol.insert_one(res)
# 4. Rearrange them with an algo from songify.py
notes = songify(dbcol)
words2 = notes

# 5. Run the default beat tracker
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
words3 = tempo

# 6. Convert the frame indices of beat events into timestamps
beat_times = librosa.frames_to_time(beat_frames, sr=sr)



def Click():
    myLabel = Label(root, text = words)
    myLabel.pack()

def Click2():
    myLabel2 = Label(root, text = words2)
    myLabel2.pack()
    custom_play_notes(words2)



def Click3():
    myLabel3 = Label(root, text = words3)
    myLabel3.pack()



myButton= Button(root, text= "click here to see the original notes", command= Click, bg="green")
myButton.pack()

myButton2= Button(root, text= "click here to see the shuffled notes", command= Click2, bg="green")
myButton2.pack()


myButton3= Button(root, text= "click here to see the tempo", command= Click3, bg="green")
myButton3.pack()

root.configure(background="yellow")


root.mainloop()


