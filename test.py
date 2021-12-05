
#!Known BUGS:

#Dependencies for this programm --- mysql.connector & Pillow // pip install
#TODO Calculator functions
import os                               
# from random import sample             #idk why are these two here, so i will remove them when i find out that they make no sense
# from re import S
import time
import sys
import mysql.connector
import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
)

slice = slice(-1) 
username = ''
password = '' 
name = ''
surname = ''
ageplus = ''
age = ''
height = ''
adding = ''
initnum = 0
lastnum = 0
num = 0
example = ''
plus = ''
minus = ''
calc_selector = ''
ageaddup = age + ageplus
whole_name = ''

#creating login and the main window - age calculator button, calculator, profile editor, profiel creator etc...
loginwindow = tkinter.Tk()
loginwindow.eval('tk::PlaceWindow . center')
mainwindow = tkinter.Tk()
mainwindow.geometry("200x200")
mainwindow.eval(f'tk::PlaceWindow . center')
mainwindow.withdraw()

def mainscreen():       #ANCHOR mainscreen
    mainwindow.configure(background='#242424')
    mainwindow.resizable(False, False)
    mainwindow.geometry('450x250')
    mainwindow.title('Project Py')
    mainwindow.deiconify()
    mainwindow.protocol("WM_DELETE_WINDOW", on_closing)

    menubg = Label(
        mainwindow,
        bg='purple',
        height='100',
        width='10'
    )
    menubg.place(anchor=NW)
    image = Image.open("menuimgs/agecalculator.png")
    resize_image = image.resize((10, 10))
    photoimage = PhotoImage(master = mainwindow, file=resize_image)
    agecalcbutton = Button(
    mainwindow,
    image=photoimage
    )
    agecalcbutton.pack()

def login():        #ANCHOR loginscreen
    username = input.get()
    sql = "SELECT * FROM passwords WHERE username = %s"
    adr = (username, )
    cursor.execute(sql, adr)
    result = cursor.fetchall()
    if len(result) > 0:
        loginwindow.withdraw()
        mainscreen()
    else:
        messagebox.showerror(title='Login Error', message='Incorrect username!')

def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')

def whole_name_from_db():
    global whole_name
    sql = "SELECT * FROM passwords WHERE username = %s"
    adr = (username, )
    cursor = mydb.cursor(buffered=True)
    cursor.execute(sql, adr)
    profilename = cursor.fetchone()
    name = profilename[1]
    surname = profilename[2]
    whole_name = name + ' ' +surname
    

def yes_no_age():       #ANCHOR Yes and no for age saving
    yes = set(['yes','y', ''])
    no = set(['no','n'])
    global age
    global ageaddup

    sql = ("SELECT age from passwords WHERE username = %s")
    adr = (username, )
    cursor.execute(sql, adr)
    age = cursor.fetchone()[0]
     
    while True:
        print('Your current age: ' + str(age))
        print('Your age after saving: ' + str(ageaddup) + '\n')
        choice = input('Do you want to save changes?(Y/N)').lower()
        if choice in yes:

           sql = "INSERT "
           age = ageaddup
           print('Saved!')
           for i in range(3, 0, -1):
                print('Exiting to menu in ' + str(i))
                time.sleep(1)
           profile()
           menu()
        elif choice in no:
           menu()
        else:
           print ("Please respond with 'yes' or 'no'" + '\n')
                    

def exitagemenu():       #ANCHOR Exitagemenu
    print('\n' + 'Type 0 to return to exit')
    exit = input()
    while not(exit.isdigit()):
        exit = input('Entered value must be a number - ')
    exit = int(exit)
    screen_clear()
    yes_no_age()
    

def menu():     #ANCHOR Menu
    profile()
    print('Type the number to corresponding function:' + '\n' + 
          '1. Age Calculator' + '\n' +
          '2. Calculator' + '\n' +
          '9. Edit your profile' + '\n'*2 +
          '0 - Exit')
    global selection 
    selection = 0
    selection = input('Select a function: ')

    while not(selection.isdigit()):
        selection = input('Entered value must be a number - ')

    selection = int(selection)    
    while not(0 <= selection <= 9):
            selection = input('Please select a number (0-10) - ')
            selection = int(selection) 
    
    if selection == 1:
        ageselection()
    if selection == 2:
        calculator() 
    if selection == 9:
        profile_editor()
    if selection == 0:
        screen_clear()
        ending()
    else:
        print('Bugged ending!!')

def ending():       #ANCHOR Ending
    yes = set(['yes','y', ''])
    no = set(['no','n'])
    while True:
        choice = ''
        choice = input('Are you sure you want to exit? (Y/n) - ').lower()
        if choice in yes:
            print('Goodbye!')
            sys.exit()
        if choice in no:
            menu()
        else:
            print ("Please respond with 'yes' or 'no'" + '\n')

def ageselection():     #ANCHOR Age selection
    global age
    global ageaddup
    screen_clear()

    sql = ("SELECT age from passwords WHERE username = %s")
    adr = (username, )
    cursor.execute(sql, adr)
    age = cursor.fetchone()[0]

    print('Your age: ' + str(age) + ('\n' * 2), end='')
    print('Select a function:' + '\n' +
            '1. + Your Age' + '\n' +
            '2. - Your Age')
    ageselection = input()

    while not(ageselection.isdigit()):
        ageselection = input('Entered value must be a number - ')

    ageselection = int(ageselection)    
    while not(0 < ageselection <= 2):
        ageselection = input('Please select a number (1-2) - ')
        ageselection = int(ageselection)

    if ageselection == 1:
        screen_clear()
        print('Type 0 for exit.' + ('\n' * 2), end='')
        print('Your age: ' + str(age))
        print('Enter a number you want to add to your age: ')
        ageplus = input()

        while not(ageplus.strip('-').isdigit()):                # TODO need to fix this loop removing -
            ageplus = input('Entered value must be a number - ')
            while str(ageplus).find('-') != -1:
                ageplus = input('Entered value must not be a negative number - ')
        
        ageplus = int(ageplus)
        ageaddup = age + ageplus 

        while ageaddup < 0:
            ageplus = input('Result would be negative age, please type again - ')
            ageplus = int(ageplus)
            ageaddup = age + ageplus
        
        if ageplus > 0:
            screen_clear()
            print('Type 0 for exit.' + ('\n' * 2), end='')
            print('Your age: ' + str(age))
            print('Your age in ' + str(ageplus) + ' years will be ' + str(ageaddup))
            if 0 < ageaddup <= 11:
                    print("In that age you'd be a child.")
                    exitagemenu()
            elif 11 < ageaddup < 18:
                    print("In that age you'd be a teenager.")
                    exitagemenu()
            elif 18 <= ageaddup < 60:
                print("In that age you'd be an adult.")
                exitagemenu()
            elif ageaddup >= 60:
                print("In that age you'd be retired.")
                exitagemenu()
        elif ageplus == 0:
                menu()

    elif ageselection == 2:
        screen_clear()
        print('Type 0 for exit.' + ('\n' * 2), end='')
        print('Your age: ' + str(age))
        print('Enter a number you want to subtract to your age: ')
        ageminus = input()

        while not(ageminus.strip('-').isdigit()):
            ageminus = input('Entered value must be a number - ')
            while str(ageminus).find('-') != -1:
                ageminus = input('Entered value must not be a negative number - ')
        
        ageminus = int(ageminus)
        subtract = int(age) - ageminus 

        while subtract < 0:
            ageminus = input('Result would be negative age, please type again - ')
            ageminus = int(ageminus)
            subtract = age - ageminus
        
        if ageminus > 0:
            screen_clear()
            print('Type 0 for exit.' + ('\n' * 2), end='')
            print('Your age: ' + str(age))
            print('Your age in ' + str(ageminus) + ' years will be ' + str(subtract))
            if 0 < subtract <= 11:
                print("In that age you'd be a child.")
                exitagemenu()
            elif 11 < subtract < 18:
                print("In that age you'd be a teenager.")
                exitagemenu()
            elif 18 <= subtract < 60:
                print("In that age you'd be an adult.")
                exitagemenu()
            elif subtract >= 60:
                print("In that age you'd be retired.")
                exitagemenu()
        elif subtract == 0:
                menu()
    elif ageselection == 0:
        menu()

def profile_editor():      #ANCHOR Profile editor
    global name
    global surname
    global whole_name
    global age
    global height
    screen_clear()
    none = set(['none','None','Abort','abort'])

    sql = "SELECT * FROM passwords WHERE username = %s"
    adr = (username, )
    cursor.execute(sql, adr)
    profile = cursor.fetchone()

    print('     /** Profile editor **\      ' + '\n')
    print('Select, what do you want to change: ' + '\n' +
          '1. Name' + '\n' +
          '2. Age' + '\n' +
          '3. Height' + '\n'*2 +
          '0 - exit')
    profile_select = input('Your selection: ') #TODO Change to while loop for checking if it is the correct number
    profile_select = int(profile_select)
    if profile_select == 1:
        screen_clear()
        print('Type 0 for exit'+ '\n'*2, end = '')
        print('Your current name - ' + whole_name + '\n')
        print('Select, what do you want to change: ' + '\n' +
              '1. Name' + '\n' +
              '2. Surname' + '\n')
        profile_select21 = int(input('Your selection: ')) #TODO Change to while loop for checking if it is the correct number
        if profile_select21 == 1:
            screen_clear()
            print('Your current name - ' + profile[1])
            newname = input("Edit your name (Type 'None' to abort) - ")
            if newname in none:
                print('Successfully aborted!')
                time.sleep(0.3)
                for i in range(3, 0, -1):
                    print('Returning to profile editor in ' + str(i))
                    time.sleep(1)
                profile_editor()
            else:
                sql = "UPDATE passwords SET name = %s WHERE username = %s"
                val = (newname, username)
                cursor.execute(sql, val)
                screen_clear()
                mydb.commit()
                whole_name_from_db()
                print('Name changed successfully!')
                print('Your new name - ' + whole_name)
                for i in range(3, 0, -1):       
                    print('Returning to profile editor in ' + str(i))
                    time.sleep(1)
                profile_editor()

        if profile_select21 == 2:
            screen_clear()
            print('Your current surname - ' + surname)
            newsurname = input("Edit your surname (Type 'None' to abort) - ")
            if newsurname in none:
                print('Successfully aborted!')
                time.sleep(0.3)
                for i in range(3, 0, -1):
                    print('Returning to profile editor in ' + str(i))
                    time.sleep(1)
                profile_editor()
            else:
                sql = "UPDATE passwords SET surname = %s WHERE username = %s"
                val = (newsurname, username)
                cursor.execute(sql, val)
                screen_clear()
                mydb.commit()
                whole_name_from_db()
                screen_clear()
                print('Surname changed successfully!')
                print('Your new name - ' + whole_name)
                for i in range(3, 0, -1):       
                    print('Returning to profile editor in ' + str(i))
                    time.sleep(1)
                profile_editor()

    elif profile_select == 2:
        sql = ("SELECT age from passwords WHERE username = %s")
        adr = (username, )
        cursor.execute(sql, adr)
        age = cursor.fetchone()[0]
        screen_clear()
        print('Type 0 for exit'+ '\n'*2, end = '')
        print('Your current age - ' + str(age) + '\n')
        profile_select22 = int(input('Enter your new age - '))      #TODO Change to while loop for checking if it is number
        if profile_select22 > 0:
            yes = set(['yes','y', ''])
            no = set(['no','n'])
            screen_clear()
            while True:
                print('Your current age: ' + str(age))
                print('Your age after saving: ' + str(profile_select22) + '\n')
                choice = input('Do you want to save changes?(Y/n)').lower()
                if choice in yes:
                    sql = "UPDATE passwords SET age = %s WHERE username = %s"
                    val = (profile_select22, username)
                    cursor.execute(sql, val)
                    mydb.commit()
                    print('Saved!')
                    for i in range(3, 0, -1):
                        print('Exiting to profile editor in ' + str(i))
                        time.sleep(1)
                    profile_editor()
                elif choice in no:
                    profile_editor()
                else:
                    print ("Please respond with 'yes' or 'no'" + '\n')
        else:
            menu()

    elif profile_select == 3:
        sql = ("SELECT height from passwords WHERE username = %s")
        adr = (username, )
        cursor.execute(sql, adr)
        height = cursor.fetchone()[0]
        mydb.commit()
        screen_clear()
        print('Type 0 for exit'+ '\n'*2, end = '')
        print('Your current height - ' + str(height) + ' cm' + '\n')
        profile_select23 = int(input('Enter your new height - '))      #TODO Change to while loop for checking if it is number
        if profile_select23 > 0:
            yes = set(['yes','y', ''])
            no = set(['no','n'])
            screen_clear()
            while True:
                print('Your current height: ' + str(height) + ' cm')
                print('Your height after saving: ' + str(profile_select23) + ' cm' + '\n')
                choice = input('Do you want to save changes?(Y/n)').lower()
                if choice in yes:
                    sql = "UPDATE passwords SET height = %s WHERE username = %s"
                    val = (profile_select23, username)
                    cursor.execute(sql, val)
                    mydb.commit()
                    print('Saved!')
                    for i in range(3, 0, -1):
                        print('Exiting to profile editor in ' + str(i))
                        time.sleep(1)
                    profile_editor()
                elif choice in no:
                    profile_editor()
                else:
                    print ("Please respond with 'yes' or 'no'" + '\n')
        else:
            menu()
    elif profile_select == 0:
        menu()

def calculator():
    global num
    global lastnum
    global example
    global initnum
    screen_clear()
    initnum = int(input('Type a number you want to begin with '))
    num = initnum
    print('1. +')
    choice = int(input())       #TODO Change to while loop for checking if it is number
    if choice == 1:
        calcplus()
        calculator2()
    
def calculator2():
    global num
    global lastnum
    global example
    global initnum
    global plus
    global calc_selector
    somevar = ''
    operator = set(['+','-','*','/'])
    screen_clear()
    # if var == 1:
    #     initnum = int(input('Type a number you want to begin with '))
    #     num = initnum
    #     var = 0
    # else:
    print('Example: ' + str(initnum) + example + ' = ' + str(num))
    print()
    print('1. +')
    print('2. -')
    print('3. *')
    print('4. /')
    print('9. Remove last action')
    print('0. Exit')
    choice = int(input())
    if choice == 1:
        calcplus()
        calculator2()
    elif choice == 2:
        calcminus()
        calculator2()
    elif choice == 3:
        calctimes()
        calculator2()
    elif choice == 4:
        calcdivision()
        calculator2()
    elif choice == 9:
            somevar = ''
            for x in example[::-1]:
                if not(x in operator):
                    somevar = somevar + x
                    somevar = somevar[::-1]
                    example = example[slice]
                    calc_selector = x
                else: 
                    calc_selector = x
                    example = example[slice]
                    if calc_selector == '+':
                        num = num - int(somevar)
                    elif calc_selector == '-':
                        num = num + int(somevar)
                    elif calc_selector == '*':
                        num = num / int(somevar)
                    elif calc_selector == '/':
                        num = num * int(somevar)
                    break
            calculator2()
    else:
        menu()
                      

def calcplus():         #ANCHOR +
    global num
    global lastnum
    global example
    global plus
    global calc_selector
    example = example + ('+')
    print('Pripocitaj cislo ku ' + str(num))
    plus = int(input())
    calc_selector = '+'
    lastnum = num
    example = example + str(plus)
    num = num + plus
        
def calcminus():         #ANCHOR -
    global num
    global lastnum
    global example
    global minus
    global calc_selector
    example = example + ('-')
    print('Subtract number to ' + str(num))
    minus = int(input())
    calc_selector = '-'
    lastnum = num
    example = example + str(minus)
    num = num - minus

def calctimes():         #ANCHOR *
    global num
    global lastnum
    global example
    global times
    global calc_selector
    example = example + ('*')
    print('Multiply number to ' + str(num))
    times = int(input())
    calc_selector = '*'
    lastnum = num
    example = example + str(times)
    num = num * times

def calcdivision():         #ANCHOR /
    global num
    global lastnum
    global example
    global division
    global calc_selector
    example = example + ('/')
    print('Devide number to ' + str(num))
    division = int(input())
    calc_selector = '/'
    lastnum = num
    example = example + str(division)
    num = num / division

def profile():      #ANCHOR Profile
    screen_clear()
    whole_name_from_db()
    sql = "SELECT * FROM passwords WHERE username = %s"
    adr = (username, )
    cursor.execute(sql, adr)
    profile = cursor.fetchone()
    print('Your name: ' + whole_name + '\n' + 
        'Your age: ' + str(profile[4]) + '\n' + 
        'Your height: ' + str(profile[5]), end='')
    print('\n' * 2, end='')

def logincheck():   #ANCHOR Logincheck
    global username
    username = input('Type your username - ')
    sql = "SELECT * FROM passwords WHERE username = %s"
    adr = (username, )
    cursor.execute(sql, adr)
    result = cursor.fetchall()
    if len(result) > 0:
        screen_clear()
        print('Welcome, ' + username + '!') 
        time.sleep(2)
        menu()
    else:
        print('Username is not correct....exiting')
        exit()

def profcreation():     #ANCHOR Profilecreation
    screen_clear()
    print('----Profile Creator----')
    username = input('Type your username - ')
    password = input('Type your password - ')

    screen_clear()
    name = input('What is your name? - ')
    while not(name.isalnum()):
        name = input('Please, ensure that you use only alphabetic letters - ')
    
    surname = input('What is your surname? - ')
    while not(surname.isalnum()):
        surname = input('Please, ensure that you use only alphabetic letters - ')


    screen_clear()
    print('Your name: ' + whole_name)

    age = input('How old are you? - ')
    while not(age.isdigit()):
        age = input('Please use only numbers - ')

    screen_clear()
    age = round(int(age))
    print('Your name: ' + whole_name + '\n' + 
        'Your age: ' + str(age))

    height = input('How tall are you? - ')
    while not(height.isdigit()):
        height = input('Please use only numbers - ')

    cursor = mydb.cursor(buffered=True)
    sql = "INSERT INTO passwords (username, password, name, surname, age, height) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (username, password, name, surname, age, height)
    cursor.execute(sql, val)


    mydb.commit()
    logincheck()

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        mainwindow.destroy()
        loginwindow.destroy()

#ANCHOR DB connection


try:
    cursor.execute("CREATE DATABASE pswds")
    print('Created DB for passwords')
except:
    mydb = mysql.connector.connect(
     host="localhost",
     user="root",
     password="",
     database="pswds"
    )


try:
    cursor = mydb.cursor()
    cursor.execute("CREATE TABLE passwords (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), surname VARCHAR(255), username VARCHAR(255), age INT, height INT, password VARCHAR(255))")
except:
    screen_clear()

cursor.execute("SELECT id FROM passwords")
# cursor.fetchall()
# profcreation()
if len(cursor.fetchall()) <= 0:
    profcreation()    
else:
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
        command=login,
    )
    button.place(relx=0.5, rely=0.7, anchor=CENTER)
    loginwindow.protocol("WM_DELETE_WINDOW", on_closing)        #Needs to be at the end to secure safe exiting

    icon = PhotoImage(file='python-original.png')
    loginwindow.iconphoto(True,icon)

    loginwindow.mainloop() 


