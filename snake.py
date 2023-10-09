from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
green = (0, 255, 0)



posX = 2
posY = 2
sense.set_pixel(posX,posY,green)


def move(pos,direction):
    if(direction == "left"):
        posX -= 1
    if(direction == "right"):
        posX += 1
    if(direction == "up"):
        posY -= 1
    if(direction == "down"):
        posY += 1

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
            sense.set_pixel(posX,posY,green)




