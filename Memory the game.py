#Memory the game
#By: Dhrumilkumar Parikh
import simplegui
import random

def all_same(deck):
    return all(val == deck[0] for val in deck)

def new_game():
    global card1,card2,cards,state,prev,exposed,turns,start,game
    card1 = [0,1,2,3,4,5,6,7]
    card2 = [0,1,2,3,4,5,6,7]
    cards = card1 + card2
    prev=99
    exposed=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    state = 0
    turns=0
    label.set_text('Turns = ' + str(turns))
    random.shuffle(cards)
    start=True
    game.set_text("Start your Game!")
    
def mouseclick(pos):
    global start,game
    if start==True:
        game.set_text("Game Started")
        global exposed,state,cards, cur_pos,turns,prev
        cur_pos =  pos[0] // 50
        exposed[cur_pos] = True

        if prev==cur_pos:
            pass
        elif state == 0:
            global first_val,first_pos
            first_val=cards[cur_pos]
            first_pos=cur_pos
            state = 1
        elif state == 1:
            global second_val,second_pos
            second_val= cards[cur_pos]
            second_pos=cur_pos
            turns+=1
            label.set_text('Turns = ' + str(turns))

            state = 2
        else:
            if first_val==second_val:
                exposed[second_pos]=True
                exposed[first_pos]=True
            else:
                exposed[second_pos]= False
                exposed[first_pos]= False
            first_val=cards[cur_pos]
            first_pos=cur_pos
            state  = 1

        prev=cur_pos
    
    if all_same(exposed)==True:
        start=False
        game.set_text("Game Over!")
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(16):
        if exposed[i]==True:
            canvas.draw_text(str(cards[i]), (20+i*50, 55), 30, 'White')
        else:
            canvas.draw_polygon([(0+50*i, 0), (50+50*i, 0), (50+50*i, 100),(0+50*i,100)], 1, 'Green','Green')
            
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")
game = frame.add_label("Start your game!")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

new_game()
frame.start()