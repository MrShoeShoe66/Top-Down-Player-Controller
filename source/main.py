# Move Player Left/Right

def MovePlayerX():
    global PlayerX
    if inputToggleVar:
        if PlayerX == 4:
            pass
        else:
            PlayerX = PlayerX + 1
    elif PlayerX == 0:
        pass
    else:
        PlayerX = PlayerX - 1

# Move Player Up/Down

def MovePlayerY():
    global PlayerY
    if inputToggleVar:
        if PlayerY == 4:
            pass
        else:
            PlayerY = PlayerY + 1
    elif PlayerY == 0:
        pass
    else:
        PlayerY = PlayerY - 1

# Toggle Direction

def toggleInputType():
    global inputToggleVar
    inputToggleVar = not (inputToggleVar)

# Call Move CMD

def a_button():
    MovePlayerX()
input.on_button_pressed(Button.A, a_button)

def ab_button():
    toggleInputType()
input.on_button_pressed(Button.AB, ab_button)

def b_button():
    MovePlayerY()
input.on_button_pressed(Button.B, b_button)

# Set varyables
PlayerX = 2
PlayerY = 2
inputToggleVar = True

# Start Program

def programLoop():
    basic.clear_screen()
    led.plot(PlayerX, PlayerY)

basic.forever(programLoop)
