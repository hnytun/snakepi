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

    def render(self):
        sense.set_pixel(self.x,7,self.color)
    
    def move(self,direction):
        if(direction == "left"):
            self.x -=1
        else:
            self.x +=1
        self.render()


    


sense.clear()
ship = Ship(2,green)
while(True):
    sleep(0.5)
    
    for event in sense.stick.get_events():
        # Check if the joystick was pressed
        if event.action == "pressed":
            if(event.direction == "left"):
                ship.move("left")
            if(event.direction == "right"):
                ship.move("right")
        







