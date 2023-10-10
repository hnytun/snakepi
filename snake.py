from sense_hat import SenseHat
from time import sleep
from random import randrange


sense = SenseHat()
sense.clear()
green = (0, 255, 0)
blue = (0,0,255)
interval=0.5

#        <~~~~~~~~--
body = [[4,3],[3,3]]
sense.set_pixel(body[0][0],body[0][1],green)
sense.set_pixel(body[1][0],body[1][1],green)



#flags
currentDirection="None"
food_exist=False

def move(body,direction):

    #move body
    for i in range(len(body)-1, -1, -1):
        #ignore head
        if(i != 0):
            body[i] = body[i-1].copy()

    #move head
    if(direction == "left"):
        if(body[0][0] == 0):
            body[0][0] = 7
        else:
            body[0][0] -= 1
    if(direction == "right"):
        if(body[0][0] == 7):
            body[0][0] = 0
        else:
            body[0][0] += 1
    if(direction == "up"):
        if(body[0][1] == 0):
            body[0][1] = 7
        else:
            body[0][1] -= 1
    if(direction == "down"):
        if(body[0][1] == 7):
            body[0][1] = 0
        else:
            body[0][1] += 1
    return body



food_position = [randrange(8),randrange(8)]
first_event = sense.stick.wait_for_event()
currentDirection = first_event.direction
#main game loop
while(True):
    sleep(0.5)

    #spawn food
    if(not food_exist):
        food_position = [randrange(8),randrange(8)]
        food_exist=True

    #if(len(sense.stick.get_events()) != 0):
    for event in sense.stick.get_events():
        # Check if the joystick was pressed
        if event.action == "pressed":
            if(event.direction == "left"):
                currentDirection="left"
            if(event.direction == "right"):
                currentDirection="right"
            if(event.direction == "up"):
                currentDirection="up"
            if(event.direction == "down"):
                currentDirection="down"
    body = move(body,currentDirection)

    for bodypart in body:
        sense.set_pixel(bodypart[0],bodypart[1],green)


    if(food_exist):
        sense.set_pixel(food_position[0],food_position[1],blue)

        if(body[0] == food_position):
            body.append(food_position)
            food_exist=False

    sense.clear()



