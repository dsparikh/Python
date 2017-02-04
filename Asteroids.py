#Asteroids Final Project Game   #
#By: Dhrumilkumar Parikh        #
#################################

import simplegui #For game graphics
import math
import random

####################################################################################################################################

#GLOBAL VERIABLES
WIDTH = 800    #Game Window Frame Width
HEIGHT = 600   #Game Window Frame Width
score = 0	   #Game Score 		
lives = 3	   #Lives	
Start = False  #Start the game
time = 0	   #Timer		

####################################################################################################################################
#Image class for all the images used for Graphics
class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("https://www.dropbox.com/s/jg18y0z0h9hpkpo/Halo.mp3?raw=1")
soundtrack2= simplegui.load_sound("https://www.dropbox.com/s/9xuhbylla7f580f/Halo%20s.mp3?raw=1")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")
####################################################################################################################################

# Ship class

class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()        

    def draw(self,canvas):
        if self.thrust:
            canvas.draw_image(self.image, [135, 45], self.image_size, self.pos,self.image_size,self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos,self.image_size,self.angle)
        
    def update(self):
        forward_vec = angle_to_vector(self.angle) 
        self.angle += self.angle_vel
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        
        if self.thrust:
            self.vel[0] += forward_vec[0]*0.1
            self.vel[1] += forward_vec[1]*0.1

        self.vel[0] *= 0.99
        self.vel[1] *= 0.99

    def set_thrust(self,thrus):
        self.thrust = thrus
        if self.thrust:
            ship_thrust_sound.rewind()
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.pause()
                
    def shoot(self):
        global a_missile
        forward_vec = angle_to_vector(self.angle) 
        a_missile = Sprite([self.pos[0] + self.radius * forward_vec[0], self.pos[1] + self.radius * forward_vec[1]],[self.vel[0] + 4 * forward_vec[0], self.vel[1] + 4 * forward_vec[1]],self.angle, 0, missile_image, missile_info, missile_sound)
        missile_group.add(a_missile)
        
    def inc_ang_vel(self):
        self.angle_vel += 0.08
    
    def dec_ang_vel(self):
        self.angle_vel -= 0.08
        
    def get_position():
        return self.pos
    
    def get_radius():
        return self.radius
        
####################################################################################################################################

# Sprite class for all moving objects in the background

class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def update(self):
        self.angle += self.angle_vel
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        
        self.age+=1
        return self.age >= self.lifespan
        
    def collide(self,other_object):
        if dist(self.pos,other_object.pos) < (self.radius + other_object.radius):
            return True
        else:
            return False
        
    def get_position():
        return self.pos
    
    def get_radius():
        return self.radius
    
    def draw(self, canvas):
        center = list(self.image_center)
        if self.animated:
            center[0] = self.image_center[0] + (self.image_size[0] * self.age)
        canvas.draw_image(self.image, center, self.image_size,
                          self.pos, self.image_size, self.angle)

####################################################################################################################################

# Draw function which draws the images on the screen
           
def draw(canvas):
    global time,lives,score,rock_group,Start
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    my_ship.draw(canvas)
    my_ship.update()

    process_sprite_group(rock_group,canvas)
    process_sprite_group(missile_group,canvas)
    process_sprite_group(exploded, canvas)
    
    canvas.draw_text('Lives: '+ str(lives), (675, 25), 30, "White")
    canvas.draw_text('Score: '+ str(score), (0, 25), 30, "White")
    
    if group_collide(rock_group, my_ship):
        lives -= 1
    score += group_group_collide(missile_group, rock_group)*10
    
    if Start==False:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          splash_info.get_size())
        soundtrack.play()
        soundtrack2.pause()
        
    if lives == 0:
        rock_group = set([])
        Start = False
        soundtrack.rewind()
        soundtrack2.rewind()
        lives=3
        score=0
    
####################################################################################################################################

#Helper Functions

#converts angle to a 2D vector
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

#distance between 2 points
def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

# timer handler that spawns a rock 
def rock_spawner():
    global rock_group,Start,a_rock
    if len(rock_group) > 12 or not Start:
        return
    
    rock_pos = [random.randrange(0, WIDTH), random.randrange(0, HEIGHT)]
    while dist(rock_pos, my_ship.pos) < 100:
        rock_pos = [random.randrange(0, WIDTH), random.randrange(0, HEIGHT)] 
        
    a_rock = Sprite(rock_pos,[random.choice([1, -1]) ,random.choice([1, -1])],random.choice([0,2*math.pi]), random.choice([0.1, -0.1]), asteroid_image, asteroid_info)
    rock_group.add(a_rock)

#Draw and update rocks and missiles
def process_sprite_group(group,canvas):
    for g in group:
        g.draw(canvas)
        if g.update():
            group.remove(g)
            
#Check if 2 objects collided        
def group_collide(group,other_object):
    global exploded
    collided = False
    for this in set(group):
        if this.collide(other_object):
            group.remove(this)
            exploded.add(Sprite(this.pos, [0, 0], 0, 0, explosion_image,
                                       explosion_info, explosion_sound))
            collided = True
    return collided      

#Check if missiles and rock collided
def group_group_collide(group,other_object):
    global exploded
    score=0
    for g in set(group):
         if group_collide(other_object, g):
            group.remove(g)
            score+=1
    return score
    
# Key pressed function (key down)
def keydown(key):
    if simplegui.KEY_MAP["left"] == key:
        my_ship.dec_ang_vel()
    elif simplegui.KEY_MAP["right"] == key:
        my_ship.inc_ang_vel()
    elif simplegui.KEY_MAP["up"] == key:
        my_ship.set_thrust(True)
    elif key == simplegui.KEY_MAP['space']:
        my_ship.shoot()

#Key released function (key up)
def keyup(key):
    if simplegui.KEY_MAP["left"] == key:
        my_ship.inc_ang_vel()
    elif simplegui.KEY_MAP["right"] == key:
        my_ship.dec_ang_vel()
    elif simplegui.KEY_MAP["up"] == key:
        my_ship.set_thrust(False)
        
#Mouse click to start the game        
def click(pos):
    global Start
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (Start == False) and inwidth and inheight:
        Start = True
        soundtrack.pause()
        soundtrack2.play()

####################################################################################################################################
        
#Simplegui library commands to make the graphis and start the game        
        
# initialize and draw the frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

# initialize ship and sets of objects
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], -1.5708, ship_image, ship_info)
rock_group = set([])
missile_group = set([])
exploded = set([])

#keys and mouse 
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(click)

#Start the frame window of the game and the timer 
timer = simplegui.create_timer(2000.0, rock_spawner)
timer.start()
frame.start()
####################################################################################################################################