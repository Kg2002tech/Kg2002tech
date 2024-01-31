import tkinter as tk
import os
from pygame import mixer, mixer_music

class MusicPlayer:
     def __init__(self):
          self.songs_list = []
          self.alphabetical_order = {}
          
          self.app = tk.Tk()
          self.app.geometry('300x300')
          self.app.title('MY Music Player 1.0')
          self.app.configure(bg='black')
#BUTTONS  
    
          
          play_button = tk.Button(self.app,text="Play",fg="Blue",font=('arial',20),command=self.playSong)
          play_button.grid(row=1,column=0)
          play_button.configure() 

          pause_button = tk.Button(self.app,text='Pause',fg="Blue",font=('arial',20),command=self.pause_song)
          pause_button.grid(row=1,column=1)
          pause_button.configure()

          skip_button = tk.Button(self.app,text="Skip",fg="Blue",font=('arial',20),command=self.skip_song)
          skip_button.grid(row=1,column=2)
          skip_button.configure()
          
          stop_button = tk.Button(self.app,text='Stop',fg="Blue",font=('arial',20),command=self.stopSong)
          stop_button.grid(row=1,column=3)
          stop_button.configure()

          resume_button = tk.Button(self.app,text='Resume',fg="Blue",font=('arial',20),command=self.resume_song)
          resume_button.grid(row=1,column=4)
          resume_button.configure()

          exit_button = tk.Button(self.app,text="Exit App ",fg="Blue",font=('arial',20),command=self.exit)
          exit_button.grid(row=1,column=5)
          exit_button.configure()

     
          #initialize the mixer
          mixer.init()

#Play the song
     def playSong(self):
        path = os.chdir('C:/Users/ADMIN/Music')
        
        self.songs_list = os.listdir(path)
        for songs in self.songs_list:
            song_id_list = [] 
            self.alphabetical_order = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
            for song_letter ,song_number in self.alphabetical_order.items():
                 song_id_list.append(song_number) 
                 first_song_check = songs[0] #shows the first starting letter or number of the song 
               
                 try: 
                   if first_song_check.upper() == song_letter:
                       self.current_song = 0
                       mixer.music.set_volume(0.8)
                       for num in range(0,26,song_number+1):
                           self.current_song = 1+num
                           mixer.music.load(self.songs_list[self.current_song])
                           mixer.music.play()
                       
                 except Exception  as e:
                    print(f'BUG : {e}')
                    exit()
                        
  #Second command
     def skip_song(self):
        try:
         if self.playSong:
             
            
             #stop current song and move to next

             self.current_song += 1
             mixer.music.load(self.songs_list[self.current_song])
             mixer_music.play()
             if self.current_song > 1000:
                 self.current_song = 0
                 
        
        except Exception as e:
                print(f"BUG2 :{e}. Please play song first before skipping ")
               

     def pause_song(self):  
         mixer.music.pause()
     
     def stopSong(self):
          mixer.music.stop()

     def resume_song(self):
          mixer.music.unpause()

         


     def exit(self):
          self.app.destroy()

     def runapp(self):
          self.app.mainloop()


my_app = MusicPlayer()
my_app.runapp()

