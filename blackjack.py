# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
deck = None
dealer = None
player = None
msg = 'Hit or Stand?'

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []	# create Hand object

    def __str__(self):
        # return a string representation of a hand
        cardInHand = ""
        if len(self.hand) > 0:
            for card in self.hand:
                cardInHand += " " + str(card)
            return "Hand contains" + cardInHand
        else:
            return "Hand contains"

    def add_card(self, card):
        self.hand.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        value = 0
        hasAce = False
        for card in self.hand:
            if str(card)[1:] == 'A':
                hasAce = True
            value += VALUES.get(str(card)[1:],0)
        if hasAce:
            if value + 10 <= 21:
                return value + 10
            else:
                return value
        else:
            return value
        
        return value
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        cardNum = 0
        for card in self.hand:
            cardNum += 1
            card.draw(canvas,[pos[0] + (cardNum * CARD_SIZE[0]), pos[1]])
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []	# create a Deck object
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)    # use random.shuffle()

    def deal_card(self):
        return self.deck.pop(-1)	# deal a card object from the deck
    
    def __str__(self):
        # return a string representing the deck
        cardInDeck = ""
        for card in self.deck:
            cardInDeck += " " + str(card)
        return "Deck contains" + cardInDeck



#define event handlers for buttons
def deal():
    global outcome, in_play, deck, dealer,score, player, msg, outcome

    if in_play:
        outcome = 'You lose.'
        score -= 1
        msg = 'New Deal?'
        in_play = False
    else:
        #init deck and shuffle
        deck = Deck()
        deck.shuffle()
        #init dealer and deal 2 cards
        dealer = Hand()
        dealer.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        #init player and deal 2 cards
        player = Hand()
        player.add_card(deck.deal_card())
        player.add_card(deck.deal_card())
        in_play = True
        msg = 'Hit or Stand?'
        outcome = ''

def hit():
    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update in_play and score
    global in_play, score, msg, outcome
    if in_play:
        player.add_card(deck.deal_card())
        if player.get_value() > 21:
            outcome = "You lose."
            in_play = False
            score -= 1
            msg = 'New Deal?'
    
       
def stand():
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score
    global in_play, score, msg, outcome
    if in_play:
        while dealer.get_value() < 17:	
            dealer.add_card(deck.deal_card())
        if dealer.get_value() > 21 or player.get_value() > dealer.get_value():
            outcome =  "You won."
            in_play = False
            score += 1
            msg = 'New Deal?'
        else:
            outcome = "You lose."
            in_play = False
            score -= 1
            msg = 'New Deal?'
                

# draw handler    
def draw(canvas):
    #draw text BlackJack
    canvas.draw_text('Blackjack',(50, 50), 72, 'Cyan')
    #score
    canvas.draw_text('Score ' + str(score),(400, 50), 52, 'Black')
    # draw dealer hand
    canvas.draw_text('Dealer',(10, 240), 52, 'Black')
    canvas.draw_text(outcome,(250, 240), 52, 'Black')
    dealer.draw(canvas, [10, 250])
    if in_play:
        card_loc = (CARD_BACK_CENTER[0],CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_SIZE, [10 + CARD_BACK_SIZE[0] + CARD_BACK_CENTER[0], 250 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
    # draw player hand
    canvas.draw_text('Player',(10, 480), 52, 'Black')
    canvas.draw_text(msg,(250, 480), 52, 'Black')
    player.draw(canvas, [10, 500])

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()


# remember to review the gradic rubric