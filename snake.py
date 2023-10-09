from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()
green = (0, 255, 0)


body = [[3,3],[4,3]]
sense.set_pixel(body[0][0],body[0][1],green)


def move(body,direction):

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

    #move rest of body
    for i in range(len(body)-1, -1, -1):
        #ignore head
        if(i != 0):
            print(body[i], " at bodypart nr ", i, " gets position of ", body[i-1], " at bodypart ",i-1)
            body[i] = body[i-1].copy()

    print(body)
    return body

#main game loop
while(True):

    for event in sense.stick.get_events():
        # Check if the joystick was pressed
        if event.action == "pressed":
            if(event.direction == "left"):
                body = move(body,"left")
            if(event.direction == "right"):
                body = move(body,"right")
            if(event.direction == "up"):
                body = move(body,"up")
            if(event.direction == "down"):
                body = move(body,"down")
            sense.clear()
            for bodypart in body:
                sense.set_pixel(bodypart[0],bodypart[1],green)




