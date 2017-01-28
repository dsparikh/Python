# Blackjack casino game
# By: Dhrumilkumar Parikh

import simplegui
import random


CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

in_play = False
outcome = ""
score = 0
outcome = "To start click Deal"
your_val=0        

SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

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
        
class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        val='Hand contains'
        for card in self.hand:
            val += " " + card.__str__()
           
        return val
        
    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        value=0
        has_ace= False
        for card in self.hand:
            val = card.get_rank()
            if val == "A":
                has_ace=True
            value += VALUES[val]
        
        if value <11 and has_ace:
            value += 10
            
        return value           
         
    def draw(self, canvas, pos):
        for card in self.hand:
            card.draw(canvas,pos)
            pos[0]+=80
 
players_hand = Hand()
dealers_hand = Hand()  
 
class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)
        

    def deal_card(self):
        return self.deck.pop(0)
    
    def __str__(self):
        val = "Deck contains"
        for card in self.deck:
            val += " " + card.__str__()
        return val

def deal():
    global in_play, deck, players_hand, dealers_hand,outcome,score,your_value
    outcome = ''
    
    if in_play == False:
        deck = Deck()
        deck.shuffle()
        players_hand = Hand()
        dealers_hand = Hand()  
        players_hand.add_card(deck.deal_card())
        players_hand.add_card(deck.deal_card())
        dealers_hand.add_card(deck.deal_card())
        dealers_hand.add_card(deck.deal_card())
        your_val = players_hand.get_value()    
        in_play = True
    else:
        outcome = "You dealed again you loose!"
        score -= 1
        in_play = False

def hit():
    global in_play, deck, players_hand, dealers_hand,outcome,score,your_value

    if in_play:
        if players_hand.get_value() <= 21:
            players_hand.add_card(deck.deal_card())
        if players_hand.get_value() > 21:
            in_play = False
            score -= 1
            outcome = "You have busted. New deal?"
    your_val = players_hand.get_value()   
       
def stand():
    global in_play, deck, players_hand, dealers_hand,outcome,score,your_value
    
    if in_play:
        while dealers_hand.get_value() < 17:
            dealers_hand.add_card(deck.deal_card())

        if dealers_hand.get_value() > 21:
            score+=1
            outcome = "Dealer busted. You Win!"
        else:
            if dealers_hand.get_value() >= players_hand.get_value() or players_hand.get_value() > 21:
                score-=1
                outcome = "Dealer wins."
            else:
                score+=1
                outcome = "You win!"
    in_play = False 
    your_val = players_hand.get_value() 


def draw(canvas):
    global in_play, deck, players_hand, dealers_hand,outcome,score,your_value
    your_val = players_hand.get_value()    
    canvas.draw_text("Blackjack Table", [175, 40], 40 ,"White")
    canvas.draw_text(outcome,[200,500],20,"White")
    
    canvas.draw_text("Your Score: " +str(score),[0,500],20,"White")
    canvas.draw_text("Your value: " +str(your_val),[0,450],20,"White")
    
    players_hand.draw(canvas, [100, 300])
    dealers_hand.draw(canvas, [100, 150])
    
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, (136,199), CARD_BACK_SIZE)
        canvas.draw_text("Hit or Stay?",[200,500],20,"White")


frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

frame.start()
#Play the game online at :http://www.codeskulptor.org/