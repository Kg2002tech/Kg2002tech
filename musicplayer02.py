import tkinter as tk
import os
from pygame import  mixer
my_app = tk.Tk()
my_app.title("Music Player Alt Version 2")
my_app ['bg'] = "black"

#Initialize mixer
mixer.init()

path = os.chdir('C:/Users/ADMIN/Music')
songs_list = os.listdir(path)
current_song_index = 0

label2 = tk.Listbox(my_app,fg="Blue",font=('Helvetica',20),width=40)
label2.grid(row=1,columnspan=1)

#Display currently Playing music
mess_label = tk.Label(my_app,fg="Blue",font=('Helvetica',20),width=40)
mess_label.grid(row=2)


def playSong():
    
        mixer.music.load(songs_list[current_song_index])
        mixer.music.play()
        mess_label.configure(text=f"Playing : {songs_list[current_song_index]}")
        for songs in songs_list:
              label2.insert(tk.END,songs)


def skipSong():
        if playSong:
                 mixer.music.stop()
                 global current_song_index
                 current_song_index += 1  
                 mixer.music.load(songs_list[current_song_index])
                 mixer.music.play()
                 mess_label.configure(text=f"Playing: {songs_list[current_song_index]}")
                 
    
                     
def  pauseSong():
     mixer.music.pause()

def  resumeSong():
     mixer.music.unpause()   

def exitApp():
    my_app.destroy()


#Butttons
play_btn = tk.Button(my_app,text="PLAY ",fg="Blue",font=('arial',20),command=playSong,padx=7,pady=7)
play_btn.grid(row=3,column=1)
play_btn.configure()

skip_btn = tk.Button(my_app,text="SKIP ",fg="Blue",font=('arial',20),command=skipSong,padx=6,pady=6)
skip_btn.grid(row=3,column=2)
skip_btn.configure()

pause_btn = tk.Button(my_app,text="PAUSE ",fg="Blue",font=('arial',20),command=pauseSong,padx=7,pady=7)
pause_btn.grid(row=3,column=3)
pause_btn.configure()

resume_btn = tk.Button(my_app,text="RESUME ",fg="Blue",font=('arial',20),command=resumeSong,padx=7,pady=7)
resume_btn.grid(row=3,column=4) 
resume_btn.configure()
exit_btn = tk.Button(my_app,text="Exit ",fg="Blue",font=('arial',20),command=exitApp,padx=7,pady=7)
exit_btn.grid(row=3,column=5)
exit_btn.configure()
def runApp():
    my_app.mainloop()
runApp()
