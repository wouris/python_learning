import time
import os
import sys
import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

if sys.argv:
    filepath = sys.argv[0]
    folder, filename = os.path.split(filepath)
    os.chdir(folder)

mainwindow = tkinter.Tk()
mainwindow.geometry("200x200")
mainwindow.eval(f'tk::PlaceWindow . center')

mainwindow.configure(background='#242424')
mainwindow.resizable(False, False)
mainwindow.geometry('650x350')
mainwindow.title('Project Py')
mainwindow.deiconify()
# mainwindow.protocol("WM_DELETE_WINDOW", closing_window)

menubg = Frame(
    mainwindow,
    bg='purple',
    height='100',
    width='10'
)
menubg.pack(side = LEFT)

photoimage = PhotoImage(master = mainwindow, file='menuimgs/account.png')

accountbutton = Button(
    mainwindow,
    bg = 'purple',
    fg = 'purple',
    bd = 0,
    activebackground='purple',
    image=photoimage,
    height=100,
    width=100,
)
accountbutton.pack(side = TOP)

mainwindow.mainloop()