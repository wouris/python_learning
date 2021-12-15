import random
import os
import time

def clrscr():   #clearing the screen
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')

def stage(stage):
    if stage == 1:
        print(
            '\n'*4 +
            '_______' + '\n' +  
            '|     |' + '\n' +
            '|     |'+ '\n')
        
    elif stage == 2:
        print(
            '\n' +
            '   |' + '\n' +
            '   |' + '\n' + 
            '   |' + '\n' + 
            '__/ \__' + '\n' +
            '|     |' + '\n' +
            '|     |'+ '\n')
    elif stage == 3:
        print(
            '    ___________' + '\n' +
            '   |/' + '\n' +
            '   |' + '\n' + 
            '   |' + '\n' + 
            '__/ \__' + '\n' +
            '|     |' + '\n' +
            '|     |'+ '\n')
    elif stage == 4:
        print(
            '    ___________' + '\n' +
            '   |/        |' + '\n' +
            '   |         O' + '\n' + 
            '   |' + '\n' + 
            '__/ \__' + '\n' +
            '|     |' + '\n' +
            '|     |'+ '\n')
    elif stage == 5:
        print(
            '    ___________' + '\n' +
            '   |/        |' + '\n' +
            '   |         O' + '\n' + 
            '   |         |' + '\n' + 
            '__/ \__' + '\n' +
            '|     |' + '\n' +
            '|     |'+ '\n')
    elif stage == 6:
        print(
            '    ___________' + '\n' +
            '   |/        |' + '\n' +
            '   |         O' + '\n' + 
            '   |         |\ ' + '\n' + 
            '__/ \__' + '\n' +
            '|     |' + '\n' +
            '|     |'+ '\n')
    elif stage == 7:
        print(
            '    ___________' + '\n' +
            '   |/        |' + '\n' +
            '   |         O' + '\n' + 
            '   |        /|\ ' + '\n' + 
            '__/ \__' + '\n' +
            '|     |' + '\n' +
            '|     |'+ '\n')
    elif stage == 8:
        print(
            '    ___________' + '\n' +
            '   |/        |' + '\n' +
            '   |         O' + '\n' + 
            '   |        /|\ ' + '\n' + 
            '__/ \__     /  ' + '\n' +
            '|     |' + '\n' +
            '|     |'+ '\n')
    elif stage == 9:
        print(
            '    ___________' + '\n' +
            '   |/        |' + '\n' +
            '   |         O' + '\n' + 
            '   |        /|\ ' + '\n' + 
            '__/ \__     / \ ' + '\n' +
            '|     |' + '\n' +
            '|     |'+ '\n')

def tut_page(page):
    if page == 1:
        clrscr()
        print('#TUTORIAL#')
        print('Here, you will learn, how this game is coded to be played!')
        print('\n' + '(N)ext    (Q)uit')
        next_back = input('>> ')
        if next_back in Next:
            tut_page(2)
        else:
            return
        
    elif page == 2:
        clrscr()
        print('#TUTORIAL#')
        print('The word to guess is represented by a row of dashes, representing each letter of the word.')
        print('Example: ______ = Chicken')
        print('\n' + '(N)ext    (B)ack    (Q)uit')
        next_back = input('>> ')
        if next_back in Next:
            tut_page(3)
        elif next_back in Back:
            tut_page(1)
        else:
            return
        
    elif page == 3:
        clrscr()
        print('#TUTORIAL#')
        print('Each letter you have guessed correctly will be replaced at exact place, revealing a part of the word.')
        print('Example: __i__n = Chicken')
        print('\n' + '(N)ext    (B)ack    (Q)uit')
        next_back = input('>> ')
        if next_back in Next:
            tut_page(4)
        elif next_back in Back:
            tut_page(2)
        else:
            return
        
    elif page == 4:
        clrscr()
        print('#TUTORIAL#')
        print('You can guess ONE letter at a time.')
        print('Example: ______ = Chicken')
        print('         >> Ch')
        print('         Not correct letter! +1 Stage.')
        print('\n' + '(N)ext    (B)ack    (Q)uit')
        next_back = input('>> ')
        if next_back in Next:
            tut_page(5)
        elif next_back in Back:
            tut_page(3)
        else:
            return
    elif page == 5:
        while True: #while loop is necesarry here for going back here after playing all the stages
            clrscr()
            print('#TUTORIAL#')
            print('For each incorrectly guessed letter, you will move up a stage. There are 9 stages in total.' + '\n' +
                  'If you will fail to guess the word at 9th stage, you will loose' + '\n')
            print('Press P to prewiew all of the stages.')
            print('(P)lay    (N)ext    (B)ack    (Q)uit')
            next_back = input('>> ')
            if next_back in Next:
                break
            elif next_back in Back:
                tut_page(4)
                return
            elif next_back == 'p':
                for i in range(1,9+1):
                    clrscr()
                    if i == 9:
                        print('Final Stage No.9')
                    else:
                        print('Stage No.' + str(i))
                        
                    stage(i) #printing the stages
                    
                    if i == 9:
                        time.sleep(4)
                    elif i >= 4:
                        time.sleep(1)
                    else:
                        time.sleep(2)
            else:
                return
        tut_page(6) #advancing to next page is here, because quit will break the function and next will break the while true loop
    elif page == 6:
        clrscr()
        print('#TUTORIAL#')
        print('That is all :), you can go play the game now.')
        print('\n' + '(B)ack    (Q)uit')
        next_back = input('>> ')
        if next_back in Next:
            return
        elif next_back in Back:
            tut_page(5)
        else:
            return



sports = ['Acrobatics','Archery','Climbing','Cycling','Wrestling','Golf','Gymnastics','Pool','Football','Hockey','Bowling','Basketball','Snooker','Fishing','Chess','Skateboarding','Snowboarding','Skiing','Polo','Swimming','Diving','Sky Diving','Kayaking','Canoeing','Racing','Arm wrestling','Powerlifting','Sky Surfing']
animals = ['Alligator''Anaconda','Ant','Antelope','Ape','Baboon','Barracuda','Bass','Bat','Bear','Beetle','Bird','Bison','Black panther','Blue Whale','Bobcat','Buffalo','Butterfly','Buzzard','Camel','Cat','Caterpillar','Catfish','Cheetah','Chicken','Chimpanzee','Chipmunk','Cobra','Cougar','Cow','Coyote','Crab','Crane','Cricket','Crocodile','Crow','Deer','Dinosaur','Dog','Dolphin','Donkey','Dragonfly','Duck','Eagle','Elephant','Emu','Falcon','Ferret','Finch','Fish','Flamingo','Flea','Fly','Fox','Frog','Goat','Goose','Gorilla','Grasshopper','Hamster','Hare','Hawk','Hippopotamus','Hippo','Horse','Hummingbird','Husky','Kangaroo','Ladybug','Leopard','Lion','Lizard','Llama','Lobster','Mongoose','Monkey','Moose','Mosquito','Moth','Mountain goat','Mouse','Mule','Octopus','Orca','Ostrich','Otter','Owl','Ox','Panda','Parrot','Peacock','Pelican','Penguin','Pheasant','Pig','Pigeon','Polar bear','Rabbit','Raccoon','Rat','Raven','Sea lion','Sheep','Skunk','Snail','Snake','Spider','Tiger','Walrus','Whale','Wolf','Wasp','Zebra']
def startgame(topic):
    guessed = []
    word = random.choice(topic)
    wordlower = word.lower()
    
    for i in word:
        if i == ' ':
            guessed.append(' ')
        else:
            guessed.append('_')
    
    i = 1
    while True:
        clrscr()
        stage(i)
        print(''.join(guessed))
        print(word) #? uncomment this line for debugging or to cheat :P
        choice = input('>> ')
       
        
        if choice == word[0]:
            guessed.pop(0)
            guessed.insert(0, word[0])
            continue
            
        var = 1
        pos = -1
        for k in wordlower:
            pos += 1
            if choice == k:
                guessed.pop(pos)
                guessed.insert(pos, word[pos])
                var += 1
            else:
                pass
        if var > 1:
            i -= 1
        i += 1
        if i == 9:
            clrscr()
            stage(i)
            print(''.join(guessed))
            print('You lost!\n The word was: ' + word)
            exit()
            
        if choice == word or choice == wordlower or ''.join(guessed) == word:
            clrscr()
            stage(i)
            print(''.join(guessed))
            print('You won!')
            exit()
        
    

while True: #game loop
    clrscr()
    tutorial = set(['tutorial','Tutorial','Tut','tut','T','t'])
    Next = set(['Next','next','N','n'])
    Back = set(['Back','back','B','b'])
    Play = set(['Play','play','P','p'])
    
    print('Choose a topic:' + '\n' + 
      '1. Sports and Games' + '\n' +
      '2. Animals' + '\n' +
      'T. Tutorial'+ '\n'*2 +
      'q - Quit'+ '\n'
      )
    
    choice = input('>> ')
    if choice == '1':
        startgame(sports)
    elif choice == '2':
        startgame(animals)
    elif choice in tutorial:
       tut_page(1)
    elif choice == 'q':
        exit()
    else:
        print('Invalid value')
        

