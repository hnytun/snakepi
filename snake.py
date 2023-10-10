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
game_over=False
rate = 0.5
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
while(not game_over):
    sleep(rate)
    #for bodypart in body[2:]:
    #    if(body[0] == bodypart):
    #        game_over = True

    #spawn food
    if(not food_exist):
        food_position = [randrange(8),randrange(8)]
        food_exist=True


    #if(len(sense.stick.get_events()) != 0):
    for event in sense.stick.get_events():
        # Check if the joystick was pressed
        if event.action == "pressed":
            if(event.direction == "left" and currentDirection != "right"):
                currentDirection="left"
            if(event.direction == "right" and currentDirection != "left"):
                currentDirection="right"
            if(event.direction == "up" and currentDirection != "down"):
                currentDirection="up"
            if(event.direction == "down" and currentDirection != "up"):
                currentDirection="down"
    body = move(body,currentDirection)
    sense.clear()

    #works to put pixels here
    for bodypart in body:
        sense.set_pixel(bodypart[0],bodypart[1],green)


    if(food_exist):
        sense.set_pixel(food_position[0],food_position[1],green)

        if(body[0] == food_position):
            body.append(food_position)
            food_exist=False
            print("hit food!")
            rate = rate * 0.9


    for bodypart in body[1:]:
        if(bodypart == body[0] and bodypart != food_position):
            print("duplicate!")
            print(body)
            game_over = True
            sense.show_message(0.5,"game over, press any key to restart")

            first_event = sense.stick.wait_for_event()









