while front_is_clear():
    move()
turn_left()

while not at_goal():
    if front_is_clear():
        move()
    elif right_is_clear():
        turn_left()
        turn_left()
        turn_left()
        move()
    
    else:
        turn_left()
