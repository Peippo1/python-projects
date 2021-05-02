import random

## user guesses against the computer

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'guess an number between 1 and {x}: '))
        if guess < random_number:
           print("sorry guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again, Too high")

    print(f'Yay, congrats. You have guessed the number {random_number} correctly! you are a winner!')

## lets bring in the computer to guess!

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L) or correct (C) ??').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print (f'Ya the computer guessed your number, {guess}, correctly!')



computer_guess(1000)