import random

options = ('rock', 'paper', 'scissors')

print("Welcome to Rock Paper Scissors!")

while True:

    choice = input('Choose one! (rock, paper, scissors): ').lower()
#main game
    computer_choice = random.choice(options)
    print('I chose ' + computer_choice)

    if choice == computer_choice:
        print("It's a tie!")
    elif (choice == 'rock' and computer_choice == 'scissors') or \
            (choice == 'scissors' and computer_choice == 'paper') or \
            (choice == 'paper' and computer_choice == 'rock'):
        print("You won! :)")
        break
    else:
        print("You lost :(")
        break
    again = input('Do you want to play again? (yes/no) ').lower() #play again for tie
    if again == 'yes':
       continue
    elif again == 'no':
        print("Thanks for playing! Goodbye!")
        break
    else:
        print('Please type yes or no')
        break