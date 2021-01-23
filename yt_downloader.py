import tkinter as tk
import pytube
import io
from PIL import Image, ImageTk
from urllib.request import urlopen
from time import sleep

def unduh():
    yt = pytube.YouTube(str(entry.get()))
    video = yt.streams.first()
    video.download()
    label_selesai = tk.Label(master= window, text= 'Selesai')
    label_selesai.pack()
    frame_b.destroy()
    label_selesai.destroy()

def get_video():
    yt = pytube.YouTube(str(entry.get()))
    global frame_b
    frame_b = tk.Frame()
    judul_video = tk.Label(master= frame_b, text= yt.title)
    judul_video.pack()
    #image from URL
    image_url = yt.thumbnail_url
    image_bytes = urlopen(image_url).read()
    data_stream = io.BytesIO(image_bytes) #internal data file
    pil_image = Image.open(data_stream) #open as PIL image object
    pil_image = pil_image.resize((250, 150), Image.ANTIALIAS)
    tk_image = ImageTk.PhotoImage(pil_image) #convert PIL image to Tkinter PhotoImage Object
    gambar_video = tk.Label(master= frame_b, image=tk_image) #menyimpan gambar pada widget biasa
    gambar_video.image = tk_image #penting agar gambar dapat ditampilkan walaupun redundant
    gambar_video.pack()
    #download button
    btn_download = tk.Button(master= frame_b, text= 'Download', command= unduh)
    btn_download.pack()
    frame_b.pack()
    

window = tk.Tk()
window.title("Youtube Downloader")
window.geometry("500x300")

frame_a = tk.Frame()
label_a = tk.Label(master= frame_a, text= "Video URL")
label_a.pack()
entry  = tk.Entry(master= frame_a, width=75)
entry.pack()
button_getvideo = tk.Button(master= frame_a, text= "Get Video!", command= get_video)
button_getvideo.pack() 

frame_a.pack()
window.mainloop()