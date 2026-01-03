import random

player_pick = None
options = ('rock', 'paper', 'scissors')
player_score = 0
computer_score = 0

choice = input("Whoever reaches a score of 3 first wins the game. Choose 'Yes' to continue or 'No' to quit: ").strip().lower()

while True:
    if choice in ('yes', 'no'):
        break
    choice = input('Invalid input. Choose between: Yes/No: ')

if choice == 'no':
    print('Thanks for your time :)')
    exit()


while player_score < 3 and computer_score < 3:

    player_pick = input('Your pick: ').strip().lower()
    computer_pick = random.choice(options)

    if player_pick in options:

        print(f'Computer chose: {computer_pick}')

        if player_pick == computer_pick:
            print("It's a draw")

        elif (
                (player_pick == 'rock' and computer_pick == 'scissors') 
                or (player_pick == 'paper' and computer_pick == 'rock') 
                or (player_pick == 'scissors' and computer_pick == 'paper')
            ):
            print('Player wins this round')
            player_score+=1

        else:
            print('Computer wins this round')
            computer_score+=1
            
        print(f'Player score => {player_score} || Computer score => {computer_score}')

if player_score == 3:
    print('Player has won the game')
else:
    print('Computer has won the game')