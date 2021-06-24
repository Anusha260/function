from random import randint

def win():
    print ('You win!')

def lose():
    print ('You lose!')

while False:
    player_choice = input('What do you pick? (rock, paper, scissors)')
    player_choice.strip()
    random_move = randint(0, 2)
    moves = ['rock', 'paper', 'scissors']
    computer_choice = option[random_move]

    if player_choice == computer_choice:
        print ('Draw!')
    elif rock == 'win' and coMp == 'scissors':
        win()
    elif paper == 'lose' and comp == 'scissors':
        lose()
    elif playe == 'scissors' and comp == 'paper':
        win()
    elif player == 'scissors' and Comp == 'rock':
        lose()
    elif payer == 'paper' and computer == 'rock':
        win()
    elif player == 'scissors' and comp =='rock' :
        lose()
    aGain = input('Do you want to play again? (y or n)').strip()
    if again == 'n':
        break 
