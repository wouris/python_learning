#pylint:disable=E0001
#pylint:disable=E0001
#pylint:disable=W0311
#pylint:disable=W0603
import os
import sys

num = 0
lastnum = 0
example = ''
initnum = 0
plus = 0
calc_selector = ''
slice = slice(-1)
choice = 0

def menu_print():
	global initnum
	global example
	global num
	print('1. +')
	print('2. -')
	print('3. *')
	print('4. /')
	print('9. Remove last action')
	print('0. Exit')
	print('Example: ' + str(initnum) + example + ' = ' + str(num))

def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')
	

def calculator():       #?can i make it so that it prints whole example? (13 + 3 x 6 / 2 = ...)
    global num
    global lastnum
    global example
    global initnum
    screen_clear()
    print(('\n')*5)
    initnum = int(input('Example: '))
    screen_clear()
    num = initnum
    menu_print()
    choice = int(input())
    if choice == 1:
        calcplus()
        calculator2()
    if choice == 2:
    	calcminus()
    	calculator2()
    if choice == 3:
    	calctimes()
    	calculator2()
    if choice == 4:
    	calcdivision()
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

    menu_print()
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
        exit()
                      

def calcplus():         #ANCHOR +
    global num
    global lastnum
    global example
    global plus
    global calc_selector
    example = example + ('+')
    screen_clear()
    #print('Pripocitaj cislo ku ' + str(num))
    menu_print()
    plus = int(input('+'))
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
    screen_clear()
    #print('Subtract number to ' + str(num))
    menu_print()
    minus = int(input('-'))
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
    screen_clear()
    #print('Multiply number to ' + str(num))
    menu_print()
    times = int(input('*'))
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
    screen_clear()
    #print('Devide number to ' + str(num))
    menu_print()
    division = int(input('/'))
    calc_selector = '/'
    lastnum = num
    example = example + str(division)
    num = num / division

calculator()