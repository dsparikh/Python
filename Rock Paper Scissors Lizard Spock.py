#Name Dhrumilkumar Parikh
#Mini-project #1

import random
import math

def name_to_number(name)
    if name==rock
        return 0
    elif name==Spock
        return 1
    elif name==paper
        return 2
    elif name==lizard
        return 3
    elif name==scissors
        return 4
    else 
        return -1
  
def number_to_name(number)
    if number==0
        return rock
    elif number==1
        return Spock
    elif number==2
        return paper
    elif number==3
        return lizard
    elif number==4
        return scissors
    else 
        return Error 

def rpsls(player_choice) 
    
    print Player chooses  + str(player_choice)
    player_number=name_to_number(player_choice)
    
    comp_number=random.randrange(0,5)
    comp_choice=number_to_name(comp_number)
    print Computer chooses  + str(comp_choice)
    
    result=(player_number-comp_number)%5
    
    if (result==1) or (result==2)
        print Player wins!
    elif (result==3) or (result==4)
        print Computer wins!
    elif result==0
        print Player and computer tie!
    else
        print error (
        
    print 


rpsls(rock)
rpsls(Spock)
rpsls(paper)
rpsls(lizard)
rpsls(scissors)
            
