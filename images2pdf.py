import tkinter as tk
from tkinter import filedialog, Text, HORIZONTAL
from PIL import Image
import sys
import os

# FUNCTIONS

def addImg():
    for widget in frame.winfo_children():
        widget.destroy()
    filenames = filedialog.askopenfilenames(initialdir="~/",title="Select File",
    filetypes=(("images","*.jpg"),("all files","*.*")))
    for filename in filenames:
        imgs.append(filename)
        print(filename)
    for img in imgs:
        label = tk.Label(frame,text=img,bg="gray")
        label.pack()

def mergePDF():
    f = filedialog.asksaveasfile(mode='wb+', defaultextension=".pdf")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return


    for img in imgs:
        imge = Image.open(img)
        imge.save(f,"PDF",resolution=100.0,save_all=False,append_images=imge,append=True)
    print(imge)
    f.close() # `()` was missing.


def reset():
    for widget in frame.winfo_children():
        widget.destroy()
    del imgs[:]

# MAIN #    
window = tk.Tk()
imgs = []

canvas = window.geometry("400x600")
window.resizable(1, 0) 
window.title("Images to PDF")

frame=tk.Frame(window,bg="white")
frame.place(relwidth=0.8,relheight=0.7,relx=0.1,rely=0.20)

openFile = tk.Button(window,text="Open File",padx=10,pady=5,fg="white",bg="black",command=addImg)
#openFile.place(relwidth=0.1,relheight=0.1,relx=0.1,rely=0.1)
openFile.pack()

mergePDF = tk.Button(window,text="Merge Files",padx=10,pady=5,fg="white",bg="black",command=mergePDF)
#mergePDF.grid(row=0,column=2)
mergePDF.pack()

reset = tk.Button(window,text="Reset",padx=10,pady=5,fg="white",bg="black",command=reset)
#mergePDF.grid(row=0,column=2)
reset.pack()

window.mainloop()
