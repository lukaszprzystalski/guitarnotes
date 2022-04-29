import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
from functools import partial

notes_list = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
c = 0
r = 0

def notes(note):

    major_scale_steps = [2,2,1,2,2,2,1]
    minor_scale_notes = [2,1,2,2,1,2,2]

    #find where provided note is located and rearrange notes_list accordingly
    ind = notes_list.index(note)
    n_tran = notes_list[ind:]+notes_list[:ind]

    #gather notes using major_scale_steps
    major_scale = [n_tran[0],n_tran[2],n_tran[4],n_tran[5],n_tran[7],n_tran[9], n_tran[11], n_tran[0]]
    minor_scale = [n_tran[0],n_tran[2],n_tran[3],n_tran[5],n_tran[7],n_tran[8], n_tran[10], n_tran[0]]

    #gather information about chords in minor/major scale
    #print chords that are available in provided scale

    return major_scale

def clicked(note):
    #te = notes(i.config('text')[-1])
    test.config(text=notes(note))
    
    
window = tk.Tk()
window.title('Guitar notes')
window.geometry('320x250')

#place label with results
test = tk.Label(window)
test.place(x=100, y=150)

#create buttons
for i, note in enumerate(notes_list):
    btn = Button(window, text=note, command=partial(clicked, note))
    btn.config(height=2, width=10)
    btn.grid(column=c, row=r)
    c+=1
    if c == 4:
        c=0
        r+=1



window.mainloop()
