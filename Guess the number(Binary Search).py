#By: Dhrumilkumar Parikh
#Guess the Number (Binary Search)

import simplegui
import math
import random

#Default range is 100
ranges=100
guess_remaining=7

# helper function to start and restart the game
def new_game():
    global secret_number
    if ranges==100:
        global guess_remaining
        guess_remaining=7
        secret_number=random.randrange(0, 100)
        print "New game. Range is [0,100)"
    elif ranges==1000:
        guess_remaining=10
        secret_number=random.randrange(0, 1000)
        print "New game. Range is [0,1000)"
    print "Number of remaining guesses is " + str(guess_remaining)
    print ""

# define event handlers for control panel
def range100():
    global ranges
    ranges=100
    new_game()

def range1000():
    global ranges
    ranges=1000
    new_game()
    
def input_guess(guess):
    guess_int = int(guess)
    
    global guess_remaining
    guess_remaining-=1
    
    print "The guess was", guess_int
    print "Number of remaining guesses is " + str(guess_remaining)
    
    if (secret_number == guess_int):
        print "Correct \n"
        new_game()
    elif guess_remaining == 0:
        print "You ran out of guesses. " + "The number was", secret_number,"\n"
        new_game()
    elif (secret_number < guess_int):
        print "Lower\n"
    elif (secret_number > guess_int):
        print "Higher\n"
    else:
        print "Error\n"
       

frame = simplegui.create_frame('Game', 200, 200)
button1 = frame.add_button('Range is [0,100)', range100)
button2 = frame.add_button('Range is [0,1000)', range1000)
inp = frame.add_input('Enter your guess', input_guess, 50)

frame.start()
new_game()