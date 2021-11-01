import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

mainwindow = tk.Tk()    
menubg = Label(
   mainwindow,
   bg='purple',
   height='100',
   width='10'
)
menubg.place(anchor=NW)
photoimage = PhotoImage(file='account.png')
label = Label(image=photoimage)
agecalcbutton = Button(
   mainwindow,
   image=photoimage
)
agecalcbutton.pack()
#Start the program
mainwindow.mainloop()