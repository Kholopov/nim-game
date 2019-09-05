# The submission confirmation number is 6c7c7cae-ac91-436f-a0d3-2173839e47d1. 
# This program plays the game between Human and Computer for 5 rounds.
# The game consists of 3 piles of coins.
# Two players take turns to remove 1 or more coins from 1 pile.
# Each player must remove at least one coin and can choose 
# to remove any number of coins, including the whole pile. 
# The player who removes the last coin from the last pile is the winner.
#

import random

def main():

# Part A: Player Choices. The tasks are to set the initial board and get the initial player to start the game; collect the inputs for the first game

    win1=0 #the counter of wins for a human
    win2=0 #the counter of wins for a computer
    coinList = [] #the list used to store the number of coins after each move; enables updating the board
    PILE = 3 #the number of piles given in the task specification
    randCoin = random.randint(1,10) #generates random coins for the initial board

    #calling the function to generate the initial board for the first game
    initialBoard(coinList,PILE,randCoin) 

    #calling the function to get the player who starts the first game as well as determine the names of both players
    player,NAME1,NAME2=initialPlayer() 
#
# Part B: Playing the game + Part C: Validate User Input + Part E: Rounds     
# The tasks are to run the first game (including move validation and updating the board) and get the first winner;
# to continue the game for 2-4 more rounds.

    #calling the function to run the first game and get the first winner
    winner=game(coinList,PILE,randCoin,NAME1,NAME2,player)

    #calling the function to continue playing the game for 2-4 rounds, updating the scores and defining the final winner
    win1,win2=rounds(coinList, PILE, randCoin, NAME1, NAME2,win1,win2,winner) 

    #printing the final outcome                                                                        
    print ('\nFinal Outcome:\nHuman: {}\nComputer: {}'.format(win1,win2))
    if (win1 > win2):
           print ('\nYou win!')
    elif (win2 > win1):
           print ('\nComputer wins!')
    else:
           print ('\nLooks like that was a draw!')

# Functions

#a function used to set up the initial board with 3 piles and randomly generated coins in each pile
def initialBoard(coinList,PILE,randCoin): 
    print("\nLet's look at the randomly generated board.")
    print("-"*25)
    for i in range(0,PILE):
        randCoin=random.randint(1,10)
        print('PILE {}: {}'.format(i+1, '*'*randCoin))
        coinList.append(randCoin)
    print("-"*25)

#a function used to get the player who begins the game as well as the names of both players
def initialPlayer(): 
    NAME1='Human'
    NAME2='Computer'
    humanChoice=int(input('Please type 1 if you want to go first; type 2 if you want to go second: '))
    if humanChoice==1:
        player=NAME1
        print ('\n{} is player 1 and {} is player 2.'.format(NAME1,NAME2))
    elif humanChoice==2:
        player=NAME2
        print ('\n{} is player 1 and {} is player 2.'.format(NAME2,NAME1))
    return player,NAME1,NAME2     

#a function used to get a move from the current player, validate it and print the valid move; 
#it also updates the coin list after each move
def validMove(coinList,PILE,player):
    # use a loop to get a valid move
    print('\n{}, it is your turn to play.'.format(player))
    while True:
        if player=='Human':
            move=input('\nPlease type the pile number (1-3) and the number of coins you want to remove(1 to 10 inclusive) as two digits: ')
            pileNumber=move[:1]
            coins=move[1:]
            if (coins and pileNumber) and (coins.isdigit()) and (pileNumber.isdigit()):
                if (int(coins) > 0) and (int(pileNumber) > 0) and (int(pileNumber) <= len(coinList)):
                    if (int(coins) <= coinList[int(pileNumber) - 1]):
                        break
            print("You entered an invalid value. Please try again, {}.".format(player))
        elif player=='Computer':
            pileNumber=random.randint(1,3)
            coins=random.randint(1,10)
            if (coins > 0) and (pileNumber > 0) and (pileNumber <= len(coinList)):
                if (coins <= coinList[pileNumber - 1]):
                    break
    print ("\n{} has removed {} coins from pile {}, leaving the following piles:".format(player,coins,pileNumber))
    coinList[int(pileNumber)-1] -= int(coins)

#a function used to print the updated board after each move
def updatedBoard(coinList,PILE): 
    print("-"*25)
    for i in range(0,PILE):
        print('PILE {}: {}'.format(i+1, '*'*coinList[i]))
    print("-"*25)

#a function used to actually play the game; it includes doing valid moves, updating the board, 
#switching players and recording the winner at the end
def game(coinList,PILE, randCoin, NAME1,NAME2,player): 
    # use a loop to switch players
    while True:
        validMove(coinList,PILE,player)
        updatedBoard(coinList,PILE)
        # check if coin list is empty, necessary and sufficient condition to determine a winner
        if coinList == [0] * len(coinList):
            print("\n{} is the winner of this round!".format(player))
            winner=player
            break #break after the round end, to avoid switching players
        else:# switch players
            if player == NAME1:
                player = NAME2
            else:
                player = NAME1
    return winner

#a function used to continue playing for 2-4 rounds after the first game;
#it updates the scores, prints them; decides if the game must be continued; if yes, gets the input needed to run a new round and runs it
#otherwise, it terminates the game
def rounds(coinList,PILE, randCoin, NAME1,NAME2,win1,win2,winner): 
    for i in range (1,5):
        if winner==NAME1:
            win1 += 1
        elif winner==NAME2:
            win2 += 1
        print ('\nCurrent scores:\nHuman: {}\nComputer: {}'.format(win1,win2))
        if (win1 == 3 or win2 == 3):
            break 
        coinList = []
        PILE = 3
        randCoin = random.randint(1,10)
        print ('\nTime to play next round!')
        initialBoard(coinList,PILE,randCoin)
        player,NAME1,NAME2=initialPlayer()
        winner=game(coinList,PILE,randCoin,NAME1,NAME2,player)
        i=i+1
    return win1,win2

main()                        
                        
