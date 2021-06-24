#My solution to the guessing game
from random import randint
number_to_guess = randint(1,100)
guessed_number = -1
guessed_list = []

while(guessed_number != number_to_guess):
    guessed_number = int(input('Enter number: '))
    if(guessed_number < 1 or guessed_number > 100):
        print('OUT OF BOUNDS')
    else:
        if(len(guessed_list) == 0 and (abs(guessed_number - number_to_guess) <= 10)):
            print('WARM!')
        elif(len(guessed_list) > 0 and (abs(guessed_number - number_to_guess) < abs(number_to_guess - guessed_list[-1]))):
            print('WARMER!')
        elif(len(guessed_list) > 0 and (abs(guessed_number - number_to_guess) > abs(number_to_guess - guessed_list[-1]))):
            print('COLDER!')                                    
        else:
            print('COLD!')
    guessed_list.append(guessed_number)
print(f'Correct in {len(guessed_list)} guesses!')