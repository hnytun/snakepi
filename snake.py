from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
green = (0, 255, 0)



body = [[2,3],[3,3]]
sense.set_pixel(pos[0][0],pos[0][1],green)
sense.set_pixel(pos[1][0],pos[1][1],green)





def move(body,direction):

    head = body[0]
    #move head first
    if(direction == "left"):
        if(head[0] == 0):
            head[0] = 7
        else:
            head[0] -= 1
    if(direction == "right"):
        if(head[0] == 7):
            head[0] = 0
        else:
            head[0] += 1
    if(direction == "up"):
        if(head[1] == 0):
            head[1] = 7
        else:
            head[1] -= 1
    if(direction == "down"):
        if(head[1] == 7):
            head[1] = 0
        else:
            head[1] += 1

    #move rest of body

    for i in range(len(body)-1, -1, -1):
        #ignore head
        if(i != 0):
            body[i] = body[i-1]




    return pos


#main game loop
while(True):
    #sleep(1)
    for event in sense.stick.get_events():
        # Check if the joystick was pressed
        if event.action == "pressed":
            if(event.direction == "left"):
                pos = move(body,"left")
            if(event.direction == "right"):
                pos = move(body,"right")
            if(event.direction == "up"):
                pos = move(body,"up")
            if(event.direction == "down"):
                pos = move(body,"down")
            sense.clear()
            for bodypart in body:
                sense.set_pixel(bodypart[0],bodypart[1],green)




