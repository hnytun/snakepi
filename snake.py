from sense_hat import SenseHat
sense = SenseHat()

green = (0, 0, 255)

sense.clear()
sense.set_pixel(2,2,green)


while(True):
    sleep(1)
    for event in sense.stick.get_events():
        # Check if the joystick was pressed
        if event.action == "pressed":
            if(event.direction == "left"):
                print("left!")
            if(event.direction == "right"):
                print("right!")
            if(event.direction == "up"):
                print("up!")
            if(event.direction == "down"):
                print("down!")



