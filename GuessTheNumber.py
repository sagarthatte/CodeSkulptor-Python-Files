# 'Guess the number' game.
#################################################################
### Instructions for running the game
### Go to codeskulptor.org, copy paste the code, and run it.
### Some modules used in the program, only function with codeskulptor.org
#################################################################

# input will come from buttons and an input field
# all output for the game will be printed in the console

#importing required modules
import simplegui
import random

# initialize global variables
# default num range
num_range = 100
#default left guesses for num range of 100
left_guesses = 7
# global variable that increments on each guess and helps reset left_guesses
counter = 0
# secret_number is generated for default game play
secret_number = random.randrange(0, num_range)

# function to start and restart the game
def new_game():
    print "New Game. Range is from 0 to ", num_range
    print "Number of remaining guesses is ", left_guesses

# define event handlers for control panel
def range100():
    """ event handler for Range 0 to 100: button """
    global left_guesses, num_range, secret_number
    num_range = 100
    left_guesses = 7
    secret_number = random.randrange(0, num_range)
    print ""
    new_game()

def range1000():
    """ event handler for Range 0 to 1000: button """
    global left_guesses, num_range, secret_number
    num_range = 1000
    left_guesses = 10
    secret_number = random.randrange(0, num_range)
    print ""
    new_game()
    
def input_guess(guess):
    """ event handler for input_area, accepts number and 
    does computation to generate result """
    
    global secret_number, left_guesses, counter
    guess_num = int(guess)
    print ""
    print "Guess made was ", guess_num
    if guess_num < secret_number:
        counter = counter + 1
        left_guesses = left_guesses - 1
        print "Number of remaining guesses is ", left_guesses
        if left_guesses == 0:
            print "Hard Luck! Out of guesses!"
            print "Good Luck for next game.."
            left_guesses = left_guesses + counter
            secret_number = random.randrange(0, num_range)
            print ""
            new_game()
            counter = 0
        else:
            print "Make a higher guess"
    elif guess_num > secret_number:
        counter = counter + 1
        left_guesses = left_guesses - 1
        print "Number of remaining guesses is ", left_guesses
        if left_guesses == 0:
            print "Hard Luck! Out of guesses!"
            print "Good Luck for next game.."
            left_guesses = left_guesses + counter
            secret_number = random.randrange(0, num_range)
            print ""
            new_game()
            counter = 0
        else:
            print "Make a lower guess"
    elif guess_num == secret_number:
        counter = counter + 1
        left_guesses = left_guesses - 1
        print "Number of remaining guesses is ", left_guesses
        print "Correct Answer!!!"
        left_guesses = left_guesses + counter
        secret_number = random.randrange(0, num_range)
        print "" 
        new_game()
        counter = 0
        
# create frame
frame = simplegui.create_frame("Guess the Number", 200, 200)

# registering event handlers for control elements
frame.add_button("Range: 0 - 100", range100, 200)
frame.add_button("Range: 0 - 1000", range1000, 200)
frame.add_input("Player Guess", input_guess, 75)

# call new_game and start frame
new_game()
frame.start()
