from sense_hat import SenseHat
from time import sleep
from random import randrange
import threading
import os

sense = SenseHat()
green = (0,255,0)
blue = (0,0,255)
gray=(0,0,0)


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
        sense.set_pixel(self.x,7,self.color)



def projectile_task():


    x=1
    y=8
    print("Projectile assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running projectile: {}".format(os.getpid()))
    

    for i in range(7, -1, -1):
        sleep(0.5)
        sense.set_pixel(x,i-1,gray)
        sense.set_pixel(x,i,blue)

    sense.clear()

    


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







