from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
green = (0, 255, 0)



pos = [[2,3],[3,3]]
sense.set_pixel(pos[0][0],pos[0][1],green)
sense.set_pixel(pos[1][0],pos[1][1],green)

def moveHead(pos,direction):
    if(direction == "left"):
        if(pos[0] == 0):
            pos[0] = 7
        else:
            pos[0] -= 1
    if(direction == "right"):
        if(pos[0] == 7):
            pos[0] = 0
        else:
            pos[0] += 1
    if(direction == "up"):
        if(pos[1] == 0):
            pos[1] = 7
        else:
            pos[1] -= 1
    if(direction == "down"):
        if(pos[1] == 7):
            pos[1] = 0
        else:
            pos[1] += 1
    return pos


#main game loop
while(True):
    #sleep(1)
    for event in sense.stick.get_events():
        # Check if the joystick was pressed
        if event.action == "pressed":
            if(event.direction == "left"):
                pos = moveHead(pos[0],"left")
            if(event.direction == "right"):
                pos = moveHead(pos[0],"right")
            if(event.direction == "up"):
                pos = moveHead(pos[0],"up")
            if(event.direction == "down"):
                pos = moveHead(pos[0],"down")
            sense.clear()
            sense.set_pixel(pos[0],pos[1],green)




