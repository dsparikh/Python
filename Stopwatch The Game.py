# Stopwatch The Game
# By Dhrumilkumar Parikh

import simplegui
import time
import math


current_time = 0
#score xy
x=0
y=0

#Format time
def format(t)
    D=t%10
    BC=(t10)%60
    A=(t10)60
    
    if t10 or BC==0
        return (str(A) +  + 00 + . + str(D))
    elif (BC=1 and BC=9)
        return (str(A) +  + 0 +str(BC) + . + str(D))
    elif BC =10
        return (str(A) +  +str(BC) + . + str(D))
    else
        return Error
    
#Start Button
def start_handler()
    timer.start()
    
#Stop Button
def stop_handler()
    timer.stop()
    if current_time%10 == 0
        global x
        x+=1
        global y
        y+=1
    else
        y+=1
        
#Reset Button
def reset_handler()
    timer.stop()
    global current_time
    current_time=0
    global x
    x=0
    global y
    y=0


#Timer
def timer_handler()
    global current_time
    current_time+=1
    format(current_time)

#Draw
def draw_handler(canvas)
    canvas.draw_text(str(format(current_time)), (40, 100), 50, 'Red')
    canvas.draw_text(Score +str(x)+ out of +str(y), (90, 15), 15, 'White')

frame = simplegui.create_frame('Timer', 200, 200)

Start = frame.add_button('Start', start_handler)
Stop = frame.add_button('Stop', stop_handler)
Reset = frame.add_button('Reset', reset_handler)


frame.set_draw_handler(draw_handler)

timer = simplegui.create_timer(100, timer_handler)

frame.start()
