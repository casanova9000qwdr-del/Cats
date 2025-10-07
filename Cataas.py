from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

window = Tk()
window.title("Cats!")
window.geometry("600x480")

label1 = Label()
label.pack()

URL = "https://cataas.com/cat"
img = load.image(URL)

if img:
    label.config(image=img)
    label1.image = img

window.mainloop()