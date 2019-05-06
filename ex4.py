import getpass


number = getpass.getpass('Player 1, write down your number secretly: ')

for i in range(6):
    guess = raw_input('Player 2, input your guess: ')
    if (guess == number):
        print('You are right after trying for '+str(i+1)+ ' times. Program ends.')
        break
    if (guess < number):
        print('Your guess is too low!')
    if (guess > number):
        print('Your guess is too high!')

if (i == 6):
    print('You have tried 6 times and it is still wrong! The answer is ' +str(number)+ ' and program ends.')

