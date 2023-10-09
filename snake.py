from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
green = (0, 255, 0)



pos = [2,2]
sense.set_pixel(pos[0],pos[1],green)


def move(pos,direction):
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
            pos[0] = 0
        else:
            pos[1] += 1
    return pos


while(True):
    #sleep(1)
    for event in sense.stick.get_events():
        # Check if the joystick was pressed
        if event.action == "pressed":
            if(event.direction == "left"):
                pos = move(pos,"left")
            if(event.direction == "right"):
                pos = move(pos,"right")
            if(event.direction == "up"):
                pos = move(pos,"up")
            if(event.direction == "down"):
                pos = move(pos,"down")
            sense.clear()
            sense.set_pixel(pos[0],pos[1],green)




