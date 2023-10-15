from sense_hat import SenseHat
from time import sleep
from random import randrange
import threading
import os

sense = SenseHat()
green = (0,255,0)
blue = (0,0,255)



class Ship:

    def __init__(self,x,color):
        self.x=x
        self.color = color
        self.render()
    
    def move(self,direction):
        sense.clear()
        if(direction == "left"):
            self.x -=1
        else:
            self.x +=1
        self.render()

    def render(self):
        sense.set_pixel(self.x,7,self.color)



def projectile_task():

    x=1
    y=7
    print("Projectile assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running projectile: {}".format(os.getpid()))
    

    while(y>0):
        sleep(0.5)
        sense.clear(blue)
        sense.set_pixel(x,y,blue)
        y-=1

    


sense.clear()
ship = Ship(2,green)
while(True):
    
    
    for event in sense.stick.get_events():
        # Check if the joystick was pressed
        if event.action == "pressed":
            if(event.direction == "left" and ship.x > 0):
                ship.move("left")
            if(event.direction == "right" and ship.x < 7):
                ship.move("right")
            if(event.direction == "up"):
                projectile = threading.Thread(target=projectile_task, name='projectile')
                projectile.start()







