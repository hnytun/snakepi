from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()
green = (0, 255, 0)
interval=0.5

#        <~~~~~~~~--
body = [[4,3],[3,3]]
sense.set_pixel(body[0][0],body[0][1],green)
sense.set_pixel(body[1][0],body[1][1],green)



#flags
currentDirection="None"

def move(body,direction):

    #move rest of body
    for i in range(len(body)-1, -1, -1):
        #ignore head
        if(i != 0):
            print(body[i], " at bodypart nr ", i, " gets position of ", body[i-1], " at bodypart ",i-1)
            body[i] = body[i-1].copy()
    print("-----------current body----------")
    print(body)
    #move head first
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


first_event = sense.stick.wait_for_event()
currentDirection = first_event.direction
#main game loop
while(True):
    sleep(2)
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
    sense.clear()
    for bodypart in body:
        sense.set_pixel(bodypart[0],bodypart[1],green)




