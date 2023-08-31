import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas=tk.Tk()
canvas.title('My Music Player')
canvas.geometry('600x800')
canvas.config(bg='black')

rootpath='C:\\Users\lenovo\OneDrive\Desktop\songs'
pattern='*.mp3'

mixer.init()

prev_img=tk.PhotoImage(file='prev_img.png')
stop_img=tk.PhotoImage(file='stop_img.png')
play_img=tk.PhotoImage(file='play_img.png')
pause_img=tk.PhotoImage(file='pause_img.png')
next_img=tk.PhotoImage(file='next_img.png')

def select():
    label.config(text=listbox.get('anchor'))
    mixer.music.load(rootpath +'\\'+ listbox.get('anchor'))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listbox.select_clear('active')

def play_next():
    next_song=listbox.curselection()
    next_song=next_song[0]+1
    next_song_name=listbox.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(rootpath +'\\'+ next_song_name)
    mixer.music.play()

    listbox.select_clear(0,'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)

def prev_song():
    next_song=listbox.curselection()
    next_song=next_song[0]-1
    next_song_name=listbox.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(rootpath +'\\'+ next_song_name)
    mixer.music.play()

    listbox.select_clear(0,'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)

def pause_song():
    if(pausebutton['text']=='pause'):
        mixer.music.pause()

        pausebutton['text']='play'

    else:
        mixer.music.unpause()
        pausebutton['text']='pause'



listbox=tk.Listbox(canvas,fg='cyan',bg='black',width=100,font=('calibri',15))
listbox.pack(padx=15,pady=15)

label=tk.Label(canvas,text='',bg='black',fg='yellow',font=('calibri',18))
label.pack(pady=15)

top=tk.Frame(canvas,bg='black')
top.pack(padx=10,pady=5,anchor='center')

prevbutton=tk.Button(canvas,text='prev',image=prev_img,bg='black',borderwidth=0,command=prev_song)
prevbutton.pack(pady=15 , in_=top , side='left')

playbutton=tk.Button(canvas,text='play',image=play_img,bg='black',borderwidth=0,command=select)
playbutton.pack(pady=15,in_=top, side='left')

nextbutton=tk.Button(canvas,text='next',image=next_img,bg='black',borderwidth=0,command=play_next)
nextbutton.pack(pady=15,in_=top, side='left')

pausebutton=tk.Button(canvas,text='pause',image=pause_img,bg='black',borderwidth=0,command=pause_song)
pausebutton.pack(pady=15,in_=top, side='left')

stopbutton=tk.Button(canvas,text='stop',image=stop_img,bg='black',borderwidth=0,command=stop)
stopbutton.pack(pady=15,in_=top, side='left')


for i,j,k in os.walk(rootpath):
    for k1 in fnmatch.filter(k,pattern):
        listbox.insert('end',k1)

canvas.mainloop()
