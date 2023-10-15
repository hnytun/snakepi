from sense_hat import SenseHat
from time import sleep
from random import randrange
import threading
import os

sense = SenseHat()
green = (0,255,0)
blue = (0,0,255)
gray=(0,0,0)
red=(232,41,41)
invader_exist=False

class Ship:

    def __init__(self,x,y,color):
        self.x=x
        self.y=y
        self.color = color
        self.render()
    
    def move(self,direction):
        sense.set_pixel(self.x,self.y,gray)
        if(direction == "left"):
            self.x -=1
        else:
            self.x +=1
        self.render()

    def render(self):
        sense.set_pixel(self.x,self.y,self.color)


def projectile_task(ship_position_x):

    x=ship_position_x
    y=7
    print("ID of process running projectile: {}".format(os.getpid()))
    
    while(True):
        sleep(0.05)
        if(y != 7):
            sense.set_pixel(x,y,gray)
        y-=1
        if(y != -1):
            sense.set_pixel(x,y,blue)
        else:
            sense.set_pixel(x,y+1,gray)
            break
    

def invader_task():

    x=randrange(8)
    y=0
    
    
    print("ID of process running projectile: {}".format(os.getpid()))

    for i in range(8):
        sleep(1)

        sense.set_pixel(x,i,red)
        if(i != 0):
            sense.set_pixel(x,i-1,gray)

        
   
    

sense.clear()

ship = Ship(2,7,green)
while(True):

    if(not invader_exist):
        invader = threading.Thread(target=invader_task, name='invader')
        invader.start()
        invader_exist=True

    for event in sense.stick.get_events():
        # Check if the joystick was pressed
        if event.action == "pressed":
            if(event.direction == "left" and ship.x > 0):
                ship.move("left")
            if(event.direction == "right" and ship.x < 7):
                ship.move("right")
            if(event.direction == "up"):
                projectile = threading.Thread(target=projectile_task, name='projectile', args=[ship.x])
                projectile.start()







