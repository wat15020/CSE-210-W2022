import random as r
random_num = r.randint(1, 13)

play_again = "Y"
while play_again == "Y":
    guess = input('Enter a number: ')

    while int(guess) != random_num:
        print('Incorrect!')
        if int(guess) > random_num:
            print('Too high!')
        else:
            print('Too low!')
    
        guess = input('Enter a number: ')
    print('Congrats, you got it!')
    play_again = input('Do you want to play again? (Y/N) ')
