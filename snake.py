from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
green = (0, 255, 0)



pos = (2,2)
sense.set_pixel(pos[0],pos[1],green)


def move(direction,pos):
    if(direction == "left"):
        pos[0] -= 1
    if(direction == "right"):
        pos[0] += 1
    if(direction == "up"):
        pos[1] -= 1
    if(direction == "down"):
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




