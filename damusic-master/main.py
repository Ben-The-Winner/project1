# Beat tracking example

from fileinput import filename
from multiprocessing.pool import TERMINATE
from tkinter import filedialog, ttk
from tkinter.messagebox import showinfo
import librosa
from tkinter import *
from pandas import array
import pymongo
from playsound import playsound
from songify import songify
import IPython.display as ipd
import numpy as np
import soundfile as sf
from shuffling import convert_to_dict
from shuffling import load_file
from shuffling import custom_play_notes

root = Tk()
root.geometry("800x800")

def select_file():
    filetypes = (('audio files', '*.wav'),('All files', '*.*'))
    file_name = filedialog.askopenfilename(title='Choose a song',initialdir='/home/ben-123/Desktop/Ben/project1/damusic-master/the_song_files',filetypes=filetypes)

    showinfo(title='Selected File',message= file_name)
    return file_name

# open button
open_button = ttk.Button(root, text='Choose a song', command=select_file)
open_button.pack()

file_name=select_file()


title=Label(root,text="On A Better Note",bd=9,relief=GROOVE,
font=("times new roman",50,"bold"),bg="green",fg="yellow")
title.pack(side=TOP,fill=X)


result = load_file(file_name) 


def play():
    playsound(file_name, block= False)
    
def stop():
     playsound("damusic-master/note_sounds/shutup.swf.wav", block=True)  
    
     
# making a button which trigger the function so sound can be played
play_button = Button(root, text="Play the song you entered", font=("Helvetica", 20),
relief=GROOVE, command=play,bg="green")
play_button.pack(pady=20)

stop_button = Button(root, text="Stop", font=("Helvetica", 15),
relief=GROOVE, command=stop,bg="green")
stop_button.pack(pady=20)




# 1. Get the file path to an included audio example

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



myButton_original_notes= Button(root, text= "click here to see the original notes", command= click_display_original_notes, bg="green")
myButton_original_notes.pack()

myButton_shuffled_notes= Button(root, text= "click here to see the shuffled notes", command= click_play_shuffled_notes, bg="green")
myButton_shuffled_notes.pack()

myButton_tempo= Button(root, text= "click here to see the tempo", command= click_display_tempo, bg="green")
myButton_tempo.pack()

root.configure(background="yellow")


root.mainloop()


