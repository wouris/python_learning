import time
import os
import sys
import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import db

loginwindow = tkinter.Tk()
loginwindow.eval('tk::PlaceWindow . center')
mainwindow = tkinter.Tk()
mainwindow.geometry("200x200")
mainwindow.eval(f'tk::PlaceWindow . center')
mainwindow.withdraw()

if sys.argv:
    filepath = sys.argv[0]
    folder, filename = os.path.split(filepath)
    os.chdir(folder)

def closing_window():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        mainwindow.destroy()
        loginwindow.destroy()

def main():
    
    mainwindow.geometry("200x200")
    mainwindow.eval(f'tk::PlaceWindow . center')

    mainwindow.configure(background='#242424')
    mainwindow.resizable(False, False)
    mainwindow.geometry('450x250')
    mainwindow.title('Project Py')
    mainwindow.deiconify()
    mainwindow.protocol("WM_DELETE_WINDOW", closing_window)

    menubg = Label(
        mainwindow,
        bg='purple',
        height='100',
        width='10'
    )
    menubg.place(anchor=NW)
    photoimage = PhotoImage(master = mainwindow, file='menuimgs/account.png'), #file=resize_image)
    agecalcbutton = Button(
    mainwindow,
    image=photoimage
    )
    agecalcbutton.pack()

if __name__ == '__main__':
    db.db_connection() #execute db_connection function from db.py file
    # db.cursor.execute("SELECT id FROM passwords")
    # cursor.fetchall()
    # profcreation()
    # if len(cursor.fetchall()) <= 0:
    #     profcreation()    
    # else:
    loginwindow.configure(background='#cfe2f3')
    loginwindow.resizable(False, False)

    loginwindow.geometry('400x200')
    loginwindow.title('Project Py')

    label = Label(
        loginwindow, 
        text='Username', 
        font='Cascadia'
    )
    label.place(relx=0.3, rely=0.5, anchor=CENTER)

    input = Entry(
        loginwindow
    )
    input.place(relx=0.6, rely=0.5, anchor=CENTER)

    button = Button(
        loginwindow,
        text='Login',
        command=main,
    )
    button.place(relx=0.5, rely=0.7, anchor=CENTER)
    # loginwindow.protocol("WM_DELETE_WINDOW", closing_window())        #Needs to be at the end to secure safe exiting

    icon = PhotoImage(file='python-original.png')
    loginwindow.iconphoto(True,icon)
    
    loginwindow.mainloop()
    mainwindow.mainloop()