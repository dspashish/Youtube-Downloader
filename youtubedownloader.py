from tkinter import *
from pytube import YouTube
root = Tk()
root.title("YT - Downloader")

input_video = Entry(root)
input_video.pack()

def download():
    a = input_video.get()
    yt = YouTube(str(a))
    streams = yt.streams.first()
    streams.download()

btn = Button(root, text="Download", command=download)
btn.pack()
root.mainloop()

# from pytube import YouTube
# a = input("LInk PLease: ")
# yt = YouTube(a)
# stream = yt.streams.first()
# stream.download()