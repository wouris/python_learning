import os
import random
import time

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

pcardsum = 0
dcardsum = 0
def genacard(card, turn):
    global pcardsum
    global dcardsum
    
    randnum = random.choices(card_nums)
    randsym = random.choices(card_symb)

    card = randnum + randsym
    
    if randnum == ['A']:
        randnum[0] = '10'
    elif randnum == ['J']:
        randnum[0] = '10'
    elif randnum == ['Q']:
        randnum[0] = '10'
    elif randnum == ['K']:
        randnum[0] = '10'
    
    if turn == 'player':
        for i in randnum:
            pcardsum += int(i)
    elif turn == 'dealer':
        for i in randnum:
            dcardsum += int(i)
    
    return ' '.join(card)

yes = set(['Yes','yes', 'Y', 'y', ''])
no = set(['No', 'no', 'N', 'n'])
hit_stay = set(['hit','stay'])

money = 500
while True: #GAME STARTS
    clrscr()
    choice = input('You are starting off with $' + str(money) + '\n' + 'Would you like to start? ')
    if choice in yes:
            bet = 0
            while True:
                bet = float(input('Place your bet: '))
                if bet < 0.99:
                    print('Minimum bet is $1.' + '\n')
                elif bet > money:
                    print('Insufficient funds!')
                else:
                    break
            clrscr()
            
            cardspplayer = []
            for i in range(2):  #generating player cards
                cardspplayer.append(genacard('card', 'player'))
            print('You are dealt: ' + ", ".join(cardspplayer))
            time.sleep(2)
           
            cardsdealer = []
            for i in range(2):  #generating dealer cards
                cardsdealer.append(genacard('card', 'dealer'))
            print('The dealer is dealt: ' + ''.join(cardsdealer[:-1]) + ', XX')
            time.sleep(1)
            
            choice = None
            while not choice in hit_stay:
                choice = input('Would you like to hit or stay? ')
                if choice not in hit_stay:
                    print('That is an invalid option.')
            if choice == 'hit':
                cardspplayer.append(genacard('card', 'player'))
                print('You are dealt: ' + ", ".join(cardspplayer))
                if pcardsum > 21:
                    money -= bet
                    print(str(pcardsum) + '\n' + 'You have lost $' + str(bet))
                elif pcardsum == 21:
                    money += bet*2
                    print('Blackjack! You won $' + str(bet*2))
                elif pcardsum < 21:
                    money += bet
                    print('Blackjack! You won $' + str(bet))
            
            input('Press any key to conrinue...')
            # break   # !remove this after completion - This ends the program
        
    elif choice in no:
        print('You ended the game with $' + str(money) + '! Goodbye.')
        break