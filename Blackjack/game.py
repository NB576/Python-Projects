'''
--- Blackjack (single player) text based game ---

To-do Stretch goal:
- add functionality for ace being 1 or 11.
- add playing with multiple decks
- add multiple player functionality.
- add double down functionality.
- add split functionality.

Current game functionality:
- single player.
- player can bet if balance > 0.
- dealer follows basic blackjack rules (will hit until >= 17 or bust).
- Ace is valued at 11 only.
- dealer wins if scores are even.
- all winning bets are paid out 2:1.
'''

import os
from deck import deck
from player import player
from dealer import dealer

deck = deck()
player = player('Player',100)
dealer = dealer('Dealer')
bet = 0
round_over = False
game_over = False
replay = 'n'

#loop that contains game
while not game_over:
    #clear output, reset round,game,bet,replay variables
    os.system('clear')
    bet = 0
    round_over = False
    game_over = False 
    #print player balance, check balance not 0.
    print("Player balance: {} ".format(player.balance))
    if player.balance == 0:
        print("Balance is 0. Please come back with more funds.")
        game_over = True
        continue
    #empty player and dealer hand's:
    player.emptyHand()
    dealer.emptyHand()
    #player places a bet
    bet = player.place_bet()
    #dealer deals two cards to player and themselves.
    player.addCards(deck.initial_hand(player.name),deck.initial_hand(player.name))
    dealer.addCards(deck.initial_hand(dealer.name),deck.initial_hand(dealer.name))
    #show player hand, dealer shows one card
    player.showBothCards()
    dealer.showCard()

    #loop that contains betting process.
    while not round_over:
        #player decides to bet or stick.
        try:
            decision = input("hit or stick : ").lower()
        except:
            print("invalid action. Please choose either 'hit' or 'stick'.")
            continue 

        #player chooses hit.
        if decision ==  'hit':
            player.addCards(deck.draw_card(player.name))
            print("{0} has {1}".format(player.name,player.handValue()))

            #if player is not bust.
            if not player.isBust():
                continue   
            
            #player is bust
            else:
                print("{0} has {1} and is bust!".format(player.name,player.handValue()))
                round_over = True
                continue

        #player chooses stick.
        elif decision == 'stick':
            dealer.showBothCards()

            #loop to keep dealer hitting until handvalue >= 17
            while True:       
                #if dealer hand < 16 they hit.
                if dealer.handValue() < 16:
                    dealer.addCards(deck.draw_card(dealer.name))
                    print("{0} has {1}".format(dealer.name,dealer.handValue()))  

                #if dealer has 21 they win.
                elif dealer.handValue() == 21:
                    print("{0} has 21 (blackjack).".format(dealer.name))
                    round_over = True
                    game_over = True
                    break 

                #if dealer has >= 17 they stick.
                else:
                    print("{0} has {1}.".format(dealer.name,dealer.handValue()))
                    if(dealer.handValue() <= 21):
                        print("{} sticks.".format(dealer.name))
                    break  

        #case: invalid input
        else:
            print("invalid action. Please try again.")
            continue

        #check dealer is bust
        if dealer.isBust():
            round_over = True 
            print("{} has bust!".format(dealer.name))
            print("{0} wins. {1} added to balance.".format(player.name, 2*bet))
            #player wins and balance updated (2*bet paid).
            player.addBalance(2*bet)          
            #set round to be over
            round_over = True

        #if dealer does not bust compare scores to determine winner.
        elif dealer.handValue() >= player.handValue():
            print("{} wins".format(dealer.name))
            round_over = True
        
        #player wins and balance updated (2*bet paid).    
        else:
            print("{0} wins. {1} added to balance.".format(player.name, 2*bet))
            player.addBalance(2*bet)          
            round_over = True            

    #offer replay option
    while True:
        try:
            action = input("Play again? (Y/N): ")
            if action == 'Y':
                break
            elif action == 'N':
                game_over = True
                print("{0} walks away with balance: {1}".format(player.name,player.balance))
                print("Thanks for playing!")
            else:
                print("Invalid action. Try again.")    
                continue
            break
        except:
            print("Invalid action. Try again.")    

        
                
                   




