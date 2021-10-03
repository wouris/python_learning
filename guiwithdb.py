import tkinter
from tkinter import *
from tkinter import messagebox
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database='pswds'
)
cursor = mydb.cursor()
def login():
    username = input.get()
    sql = "SELECT * FROM passwords WHERE username = %s"
    adr = (username, )
    cursor.execute(sql, adr)
    result = cursor.fetchall()
    if len(result) > 0:
        messagebox.showinfo(title='Login', message='Welcome, ' + username + '!')
    else:
        messagebox.showerror(title='Login Error', message='Incorrect username!')

windows = tkinter.Tk()
windows.configure(background='#cfe2f3')
windows.resizable(False, False)

windows.geometry('400x200')
windows.title('Project Py')

label = Label(
    windows, 
    text='Username', 
    font='Cascadia'
)
label.place(relx=0.3, rely=0.5, anchor=CENTER)

input = Entry(
    windows
)
input.place(relx=0.6, rely=0.5, anchor=CENTER)

button = Button(
    windows,
    text='Login',
    command=login,
)
button.place(relx=0.5, rely=0.7, anchor=CENTER)

icon = PhotoImage(file='logo.png')
windows.iconphoto(True,icon)

windows.mainloop() 
