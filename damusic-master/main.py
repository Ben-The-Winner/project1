# Beat tracking example

#from fileinput import filename
from tkinter import filedialog, ttk
from tkinter.messagebox import showinfo
from tkinter import *
from playsound import playsound
from shuffling import load_file
from shuffling import custom_play_notes

root = Tk()
root.geometry("800x800")

def select_file():
    filetypes = (('audio files', '*.wav'),('All files', '*.*'))
    file_name = filedialog.askopenfilename(title='Choose a song',initialdir='/home/ben-123/Desktop/Ben/project1/damusic-master/the_song_files',filetypes=filetypes)

    showinfo(title='Selected File',message= file_name)
    return file_name


file_name=select_file()


title=Label(root,text="On A Better Note",bd=9,relief=GROOVE,
font=("times new roman",50,"bold"),bg="green",fg="yellow")
title.pack(side=TOP,fill=X)


result = load_file(file_name) 


def play():
    playsound(file_name, block= False)
     
# making a button which trigger the function so sound can be played
play_button = Button(root, text="Play the song you entered", font=("Helvetica", 20),
relief=GROOVE, command=play,bg="green")
play_button.pack(pady=20)



# 1. Get the file path to an included audio example

def click_display_original_notes():
    o_notes = Tk()
    o_notes.geometry("800x50")
    myText= result["original_notes"]

    # Add a Scrollbar(horizontal)
    h=Scrollbar(o_notes, orient='horizontal')
    h.pack(side=BOTTOM, fill='x')

    # Add a text widget
    text=Text(o_notes, font=("Calibri, 16"), wrap=NONE, xscrollcommand=h.set)
    text.pack()

    # Add some text in the text widget
    text.insert(END, myText)

    # Attach the scrollbar with the text widget
    h.config(command=text.xview)




def click_play_shuffled_notes():
    myLabel2 = Label(root, text = result["shuffled_notes"])
    myLabel2.pack()
    for i in range(4):
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


