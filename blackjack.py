#pylint:disable=W0311
#pylint:disable=W0603
#pylint:disable=W0621
import os
import random
import time

def title():
    print(
    ' _______   __                      __                 _____                      __    ' + '\n' +
'/       \ /  |                    /  |               /     |                    /  |      ' + '\n' +
'$$$$$$$  |$$ |  ______    _______ $$ |   __          $$$$$ |  ______    _______ $$ |   __ ' + '\n' +
'$$ |__$$ |$$ | /      \  /       |$$ |  /  |            $$ | /      \  /       |$$ |  /  |'+ '\n' +
'$$    $$< $$ | $$$$$$  |/$$$$$$$/ $$ |_/$$/        __   $$ | $$$$$$  |/$$$$$$$/ $$ |_/$$/ '+ '\n' +
'$$$$$$$  |$$ | /    $$ |$$ |      $$   $$<        /  |  $$ | /    $$ |$$ |      $$   $$<  '+ '\n' +
'$$ |__$$ |$$ |/$$$$$$$ |$$ \_____ $$$$$$  \       $$ \__$$ |/$$$$$$$ |$$ \_____ $$$$$$  \ '+ '\n' +
'$$    $$/ $$ |$$    $$ |$$       |$$ | $$  |      $$    $$/ $$    $$ |$$       |$$ | $$  |'+ '\n' +
'$$$$$$$/  $$/  $$$$$$$/  $$$$$$$/ $$/   $$/        $$$$$$/   $$$$$$$/  $$$$$$$/ $$/   $$/ '+ '\n'
    )

def clrscr():   #clearing the screen
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')


card_symb = [
    '\u2666', # diamond  ♦
    '\u2665', # heart    ♥
    '\u2663', # club     ♣
    '\u2660'  # spade    ♠
]
card_nums = ['A','2','3','4','5','6','7','8','9','J','Q','K']
money = 500
pcardsum = 0
dcardsum = 0
def genacard(card, turn):
    global pcardsum
    global dcardsum
    
    randnum = random.choices(card_nums)
    randsym = random.choices(card_symb)
    card = randnum + randsym
    
    if randnum == ['A']:
        randnum[0] = '11'
    elif randnum == ['J']:
        randnum[0] = '10'
    elif randnum == ['Q']:
        randnum[0] = '10'
    elif randnum == ['K']:
        randnum[0] = '10'
    
    if turn == 'player':
        for i in randnum:
            pcardsum = 21
    elif turn == 'dealer':
        for i in randnum:
            dcardsum += int(i)
    
    return ' '.join(card)

def win(bet):
    global money
    global pcardsum
    money += bet
    print('Sum: ' + str(pcardsum) + '\n' + 'You won $' + str(bet))
    
def winblackjack(bet):
    global money
    money += bet+2.5
    print('Blackjack! You won $' + str(bet*2.5))
    
def loose(bet):
    global money
    money -= bet
    print('You have lost $' + str(bet))
    
    
def dealersturn():
    while True:
        clrscr()
        print('You are dealt: ' + ', '.join(cardsplayer))
        print('Dealer is dealt: ' + ', '.join(cardsdealer))
        if dcardsum > 21:
              win(bet)
              break
        elif dcardsum <= 16:
          cardsdealer.append(genacard('card','dealer'))
        elif dcardsum >= 17:
                if dcardsum == pcardsum:
                    print('Tie. Your bet has been returned.')
                    break
                elif dcardsum < pcardsum:
                    win(bet)
                    break
                elif dcardsum > pcardsum:
                    loose(bet)
                    break

yes = set(['Yes','yes', 'Y', 'y', ''])
no = set(['No', 'no', 'N', 'n'])
hit_stay = set(['hit','stay'])

while True: #GAME STARTS
    clrscr()
    title()
    pcardsum = 0
    dcardsum = 0
    if money == 0:
        print('You lost all of your money. Please restart the game and try again.')
        exit()
    choice = input('You are starting off with $' + str(money) + '\n' + 'Would you like to start? ')
    if choice in yes:
            bet = 0
            while True:
                try:
                    bet = float(input('Place your bet: '))
                except:
                    print('Invalid input. Please try again.')
                    continue
                if bet < 0.99:
                    print('Minimum bet is $1.' + '\n')
                elif bet > money:
                    print('Insufficient funds!')
                else:
                    break
            clrscr()
            cardsplayer = []
            for i in range(2):  #generating player cards
                cardsplayer.append(genacard('card', 'player'))
            print('You are dealt: ' + ", ".join(cardsplayer))
            time.sleep(2)
            if pcardsum == 21:
                 winblackjack(bet)
                 input('Press any key to continue...')
                 continue
           
            cardsdealer = []
            for i in range(2):  #generating dealer cards
                cardsdealer.append(genacard('card', 'dealer'))
            print('The dealer is dealt: ' + ''.join(cardsdealer[:-1]) + ', XX')
            time.sleep(1)
            
            
            while True:
                choice = None
                while not choice in hit_stay:
                    choice = input('Would you like to hit or stay? ')
                    if choice not in hit_stay:
                        print('That is an invalid option.')
                if choice == 'hit':
                    cardsplayer.append(genacard('card', 'player'))
                    print('You are dealt: ' + ", ".join(cardsplayer))
                    if pcardsum > 21:
                        loose(bet)
                        break
                elif choice == 'stay':
                    dealersturn()
                    break
                            
                            
            input('Press any key to continue...')
            # break   # !remove this after completion - This ends the program
        
    elif choice in no:
        print('You ended the game with $' + str(money) + '! Goodbye.')
        exit()