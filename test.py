
#TODO Calculator functions

import os
import time
import sys
slice = slice(-1)
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
whole_name = name + surname
ageaddup = age + ageplus

def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')

def yes_no_age():       #ANCHOR Yes and no for age saving
    yes = set(['yes','y', ''])
    no = set(['no','n'])
    global age
    global ageaddup
     
    while True:
        print('Your current age: ' + str(age))
        print('Your age after saving: ' + str(ageaddup) + '\n')
        choice = input('Do you want to save changes?(Y/N)').lower()
        if choice in yes:
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
        subtract = age - ageminus 

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
            print('Your current name - ' + name)
            newname = input("Edit your name (Type 'None' to abort) - ")
            if newname in none:
                print('Successfully aborted!')
                time.sleep(0.3)
                for i in range(3, 0, -1):
                    print('Returning to profile editor in ' + str(i))
                    time.sleep(1)
                profile_editor()
            else:
                name = newname
                whole_name = name + ' ' + surname
                screen_clear()
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
                surname = newsurname
                whole_name = name + ' ' + surname
                screen_clear()
                print('Surname changed successfully!')
                print('Your new name - ' + whole_name)
                for i in range(3, 0, -1):       
                    print('Returning to profile editor in ' + str(i))
                    time.sleep(1)
                profile_editor()

    elif profile_select == 2:
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
                    age = profile_select22
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
                    height = profile_select23
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

def calculator():       #?can i make it so that it prints whole example? (13 + 3 x 6 / 2 = ...)
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
    var = 1
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
                      

def calcplus():         #ANCHOR Plus
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
        
def calcminus():         #ANCHOR Minus
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

def calctimes():         #ANCHOR Minus
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

def calcdivision():         #ANCHOR Minus
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
    num = num * division

def profile():      #ANCHOR Profile
    screen_clear()
    print('Your name: ' + whole_name + '\n' + 
        'Your age: ' + str(age) + '\n' + 
        'Your height: ' + str(height), end='')
    print('\n' * 2, end='')

screen_clear()
name = input('What is your name? - ')
while not(name.isalnum()):
    name = input('Please, ensure that you use only alphabetic letters - ')


surname = input('What is your surname? - ')
while not(surname.isalnum()):
    surname = input('Please, ensure that you use only alphabetic letters - ')

whole_name = name + ' ' + surname
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

menu()

