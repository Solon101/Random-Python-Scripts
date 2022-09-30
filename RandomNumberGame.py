#random number game
import random
SecretNum = random.randint(1,20)

print('Hello! What is your name?')

name = input()

print('Hello ' + name + ' I am thinking of a number 1-20. You have 10 guesses')

for guesses in range(1, 10):
    print('Take a guess.')
    guess = int(input())
    try:
        if guess < SecretNum:
            print('Your guess is too low')
        elif guess > SecretNum:
            print('Your guess is too high')
        else:
            break # This condition is for the correct guess
    except:
        print('Please only use numbers 1-20 and no letters')

if guess == SecretNum:
    print('Congrats, ' + name + '! The number was ' + str(SecretNum) + ' it took you ' + str(guesses) + ' attempts to guess it.')
else:
    print('Nope. Sorry the number I was thinking of was ' + str(SecretNum))
