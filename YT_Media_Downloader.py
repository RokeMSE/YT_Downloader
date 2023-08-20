from tkinter import *
from tkinter import filedialog
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.VideoFileClip import AudioFileClip
from pytube import YouTube
import threading
import shutil
import time

app = Tk()

#FUNCS 
def pdir():
    path = filedialog.askdirectory()
    btt.config(text=path)

def vid_dw():
    linkv = link.get()
    upath = btt.cget("text")
    app.title("Downloading...")
    mp4 = YouTube(linkv).streams.get_highest_resolution().download()
    vid = VideoFileClip(mp4)
    vid.close()
    shutil.move(mp4, upath)
    app.title("Download Complete!")
    time.sleep(2)
    app.title("Download Another File!")


def au_dw():
    linka = link.get()
    upath = btt.cget("text")
    app.title("Downloading...")
    mp3 = YouTube(linka).streams.filter(only_audio=True).first().download()
    au = AudioFileClip(mp3)
    au.close()
    shutil.move(mp3, upath)
    app.title("Download Complete!")
    time.sleep(2)
    app.title("Download Another File!")



# GUI
## Icons and non-interactive GUI
Title = app.title('Youtube Media Downloader')
canvas = Canvas(app, width= 400, height= 400)
canvas.pack()
logo = PhotoImage(file='YTlogo.png')
logo = logo.subsample(3, 3)
 
## Interactive GUI
t1 = Label(app, text = "Paste the link here:", font= ("Montserrat Medium", 10))
t1.pack()
t2 = Label(app, text="Save to:", font= ("Montserrat Medium", 10))
t2.pack()
link = Entry(app, width= 40)
link.pack()

btt = Button(app, text= "Choose a Directory", command= pdir)
btt1 = Button(app, text= "Download Video", command= lambda: threading.Thread(target = vid_dw).start())
btt2 = Button(app, text= "Download Audio", command= lambda: threading.Thread(target = au_dw).start())
btt.pack()
btt1.pack()
btt2.pack()

#Placement
canvas.create_image(200, 60, image=logo)
canvas.create_window(200, 130, window= t1)
canvas.create_window(200, 150, window= link)
canvas.create_window(200, 190, window= t2)
canvas.create_window(200, 220, window= btt)
canvas.create_window(200, 300, window= btt1)
canvas.create_window(200, 330, window= btt2)

app.mainloop()