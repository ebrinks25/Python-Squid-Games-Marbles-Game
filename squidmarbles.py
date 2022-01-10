import random

#
#TODO nothing
#
#
#

game_in_progress = True
turns = 0
cMarbles = 10
player_score = 10

print('The game works like this: \nYou have 10 marbles and the computer has 10 marbles. You are guessing if the computer has wagered an even or odd number of marbles.  \nIf you get it right, you get the number of marbles that the computer wagered.  \nFirst person to 20 marbles wins, the other dies. \n-----------------------------------')

#Defintion of turn function
def turn():
    global player_score
    global cMarbles

    #Makes sure that the marbles in play cannot exceed 20 or go below 0
    if player_score <= cMarbles:
        tMarbles = random.randint(1, player_score)
    elif player_score > cMarbles:
        tMarbles = random.randint(1, cMarbles)

    print('Do you think that the computer selected an even or odd number of marbles? (answer \'even\' or \'odd\')')
    answer = input()

    if (answer != 'even' and answer != 'odd'):
        print('Unknown answer, please enter valid answer')
        return

    #Determines if the number of marbles the computer selected and player guessed is odd
    if ((tMarbles % 2) == 1 and answer == 'odd'):
        cMarbles = cMarbles - tMarbles
        print('You guessed ODD... CORRECT!\nThe computer wagered', tMarbles, 'marbles.\nYou win', tMarbles, 'marbles.')
        if player_score > 20:
            player_score = 20
        else:
            player_score = player_score + tMarbles

    #Determines if the number of marbles the computer selected and player guessed is even
    elif ((tMarbles % 2) == 0 and answer == 'even'):
        cMarbles = cMarbles - tMarbles
        print('You guessed EVEN... CORRECT!\nThe computer wagered', tMarbles, 'marbles.\nYou win', tMarbles, 'marbles.')
        if player_score > 20:
            player_score = 20
        else:
            player_score = player_score + tMarbles

    #Catches all the wrong answers
    else:
        cMarbles = cMarbles + tMarbles
        print('You guessed INCORRECT!\nThe computer wagered', tMarbles, 'marbles.\nYou lose', tMarbles, 'marbles.')
        if player_score < 0:
            player_score = 0
        else:
            player_score = player_score - tMarbles

#Loop that continues until game_in_progress is made False by checking the remaining marbles in play
while game_in_progress:
    print('Player has', player_score, 'marbles remaining!')
    print('Computer has', cMarbles, 'remaining!')
    if player_score > 19:
        print('You lived. You won in', turns, 'turns.')
        print('Do you want to play again? (\'yes\' or \'no\')')
        playAgain = input()
        if playAgain == 'no':
            game_in_progress = False
        else:
            game_in_progress = True
            turns = 0
            cMarbles = 10
            player_score = 10
    elif player_score < 1:
        print('You died. You made it', turns, 'turns.')
        print('Do you want to play again? (\'yes\' or \'no\')')
        playAgain = input()
        if playAgain == 'no':
            game_in_progress = False
        else:
            game_in_progress = True
            turns = 0
            cMarbles = 10
            player_score = 10
    else:
        turn()
        turns = turns + 1
    print('-------------------------------------------')
