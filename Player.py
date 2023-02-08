#Importations des librairies et des annexes.
from pygame import mixer
from tkinter import *
import random
import tkinter.font as font
from tkinter import filedialog
#définition des fonctions
def sounddown():
    res = mixer.music.get_volume() - 0.1
    if res<0:
        res = 0
    mixer.music.set_volume(res)
def soundup():
    res = mixer.music.get_volume() + 0.1
    if res>1.0:
        res = 1.0
    mixer.music.set_volume(res)
def draw():
    temp_song=filedialog.askopenfilenames(initialdir="Music/",title="Choose a song", filetypes=(("mp3 Files","*.mp3"),))
    for s in temp_song:
        songs_list.insert(END,s)
     
def delete():
    curr_song=songs_list.curselection()
    songs_list.delete(curr_song[0])
def Previous():
    previous_one=songs_list.curselection()
    previous_one=previous_one[0]-1
    temp2=songs_list.get(previous_one)
    temp2=f'{temp2}'
    mixer.music.load(temp2)
    mixer.music.play()
    songs_list.selection_clear(0,END)
    songs_list.activate(previous_one)
    songs_list.selection_set(previous_one)
def Play():
    song=songs_list.get(ACTIVE)
    song=f'{song}'
    mixer.music.load(song)
    mixer.music.play()
def Pause():
    mixer.music.pause()
def Stop():
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)
def Resume():
    mixer.music.unpause()
def Next():
    next_one=songs_list.curselection()
    next_one=next_one[0]+1
    temp=songs_list.get(next_one)
    temp=f'{temp}'
    mixer.music.load(temp)
    mixer.music.play()
    songs_list.selection_clear(0,END)
    songs_list.activate(next_one)
    songs_list.selection_set(next_one)

#Fonction principale du programmen de: lecteur de musique.
fenetre=Tk()
playbutton = PhotoImage(file = r"resources/play.png")
pausebutton = PhotoImage(file = r"resources/pause.png")
deletebutton = PhotoImage(file = r"resources/delete.png")
drawbutton = PhotoImage(file = r"resources/draw.png")
stopbutton = PhotoImage(file = r"resources/stop.png")
previousbutton = PhotoImage(file = r"resources/previous.png")
nextbutton = PhotoImage(file = r"resources/next.png")
sounddownbutton = PhotoImage(file = r"resources/sounddown.png")
soundupbutton = PhotoImage(file = r"resources/soundup.png")
resumebutton = PhotoImage(file = r"resources/resume.png")
fenetre.title("Scarlet Music Player")
mixer.init()
mixer.music.set_volume(1.0)
fenetre.geometry("1080x720")
fenetre.resizable(width=False,height=False)
fenetre.iconbitmap("resources/icon.ico")
#boutons au dessus
draw_button=Button(fenetre,text="",image=drawbutton,command=draw)
draw_button.grid(row=0,column=0)
delete_button=Button(fenetre,text="",image=deletebutton,command=delete)
delete_button.grid(row=0,column=1)
#liste de lecture
songs_list=Listbox(fenetre,selectmode=SINGLE,bg="black",fg="white",font=('arial',15),height=25,width=98,selectbackground="gray",selectforeground="black")
songs_list.grid(columnspan=9)
songs_list.insert(END,"Music/Approaching_Nirvana/Cherry_Blossoms_Approaching_Nirvana.mp3")
songs_list.insert(END,"Music/Jpop/Kimigamitayumenomonogatari.mp3")
songs_list.insert(END,"Music/Metal/Wintersun _Beautiful_Death.mp3")
songs_list.insert(END,"Music/OST/FFBE/Final_Fantasy_Brave_Exvius_Main.mp3")
songs_list.insert(END,"Music/XC_Engage_the_Enemy.mp3")
#boutons en dessous
previous_button=Button(fenetre,text="",image=previousbutton,command=Previous)
previous_button.grid(row=2,column=0)
play_button=Button(fenetre,text="",image=playbutton,command=Play)
play_button.grid(row=2,column=1)
pause_button=Button(fenetre,text="",image=pausebutton,command=Pause)
pause_button.grid(row=2,column=2)
stop_button=Button(fenetre,text="",image=stopbutton,command=Stop)
stop_button.grid(row=2,column=3)
resume_button=Button(fenetre,text="",image=resumebutton,command=Resume)
resume_button.grid(row=2,column=4)
loop_button=Button(fenetre,text="",image=sounddownbutton,command=sounddown)
loop_button.grid(row=2,column=5)
random_button=Button(fenetre,text="",image=soundupbutton,command=soundup)
random_button.grid(row=2,column=6)
next_button=Button(fenetre,text="",image=nextbutton,command=Next)
next_button.grid(row=2,column=7)
fenetre.mainloop()