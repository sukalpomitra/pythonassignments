# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

number_guessed = 0
secret_number = 0
range_upto = 100
max_guess=7
guess_used = 0
    

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global range_upto
    global guess_used
    guess_used = 0
    secret_number = random.randrange(0,range_upto)
    print
    print "Welcome to Guess The Number Game"
    print "Guess a Number between 0 and", str(range_upto) 


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range_upto
    global max_guess
    max_guess = 7
    range_upto = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range_upto
    global max_guess
    max_guess = 10
    range_upto = 1000
    new_game()

''' Event handler '''   
def input_guess(guess):
        try:
            global secret_number
            global number_guessed
            global max_guess
            global guess_used
            number_guessed = int(guess)
            print "Guess was", guess
            if number_guessed > secret_number:
                print "Lower"
            elif number_guessed < secret_number:
                print "Higher"
            else:
                print "Correct"
                new_game()
                return
            guess_used = guess_used + 1
            if guess_used == max_guess:
                print "Sorry no more guesses left"
                new_game()
            else:
                if max_guess-guess_used == 1:
                    print "You have 1 guess left"
                else:
                    print "You have %s guesses still left" %str(max_guess-guess_used)
        except:
            number_guessed = -9999
            print "Please guess a number."

    
# create frame
frame = simplegui.create_frame("Guess The Number",800,600)

# register event handlers for control elements and start frame
frame.add_button("Range: 0 - 100",range100,200)
frame.add_button("Range: 0 - 1000",range1000,200)
frame.add_input("Enter Guess:",input_guess,200)
frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric