# implementation of card game - Memory

import simplegui
import random



# helper function to initialize globals
def new_game():
    global deck
    global exposed
    global matched
    global cardDrawn
    global cardDrawnIdx
    global turns
    global state
    cards1 = range(0,8)
    cards2 = range(0,8)
    deck = list()
    matched = list()
    cardDrawn = list()
    cardDrawnIdx = list()
    exposed = [False] * 16
    state = 0
    turns = 0
    deck = cards1 + cards2
    random.shuffle(deck)

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed
    global state
    global turns
    if exposed[pos[0] / 50] == False:
        if state == 0:
            exposed[pos[0] / 50] = True
            cardDrawn.append(deck[pos[0] / 50])
            cardDrawnIdx.append(pos[0] / 50)
            turns += 1
            state = 1
        elif state == 1:
            exposed[pos[0] / 50] = True
            if deck[pos[0] / 50] in cardDrawn:
                matched.append(cardDrawnIdx.pop())
                matched.append(pos[0] / 50)
                cardDrawn.pop()
            else:
                cardDrawn.pop()
                cardDrawnIdx.pop()
            state = 2
        else:
            exposed = [False] * 16
            for idx in matched:
                exposed[idx] = True
            exposed[pos[0] / 50] = True
            cardDrawn.append(deck[pos[0] / 50])
            cardDrawnIdx.append(pos[0] / 50)
            turns += 1
            state = 1    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    n = 5
    for i in range(16):
        if exposed[i] == False:
            canvas.draw_polygon([(n - 5,0),(n - 5,100),(n + 45,100),(n + 45, 0)],1, "Black", "Green")
        else:
            canvas.draw_text(str(deck[i]),[n,75],75,"White")
        n = n + 50
        label.set_text("Turns = " + str(turns))


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric