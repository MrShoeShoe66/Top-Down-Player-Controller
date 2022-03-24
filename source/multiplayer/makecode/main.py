# Move Player Left/Right
def MovePlayerX():
    global PlayerX
    if inputToggleVar:
        if not (PlayerX == 4):
            PlayerX = PlayerX + 1
    elif not (PlayerX == 0):
        PlayerX = PlayerX - 1

# Move Player Up/Down
def MovePlayerY():
    global PlayerY
    if inputToggleVar:
        if not (PlayerY == 4):
            PlayerY = PlayerY + 1
    elif not (PlayerY == 0):
        PlayerY = PlayerY - 1

# Call Move CMD

def on_button_pressed_a():
    MovePlayerX()
    sendUserData()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    toggleInputType()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    MovePlayerY()
    sendUserData()
input.on_button_pressed(Button.B, on_button_pressed_b)

# Toggle Direction

def toggleInputType():
    global inputToggleVar
    inputToggleVar = not inputToggleVar

# Set varyables

PlayerX = 2
PlayerY = 2
inputToggleVar = True
OtherX = 2
OtherY = 2

# Start MultiPlayer

radio.set_transmit_power(5)
radio.set_group(194)

def verifiyConection():
    radio.send_value("ping", 0)

verifiyConection()

def sendUserData():
    radio.send_value("x", PlayerX)
    radio.send_value("y", PlayerY)

def getMultiPlayerData(name, value):
    global OtherX, OtherY
    if name == "x":
        OtherX = value
    elif name == "y":
        OtherY = value
    elif name == "ping":
        sendUserData()

radio.on_received_value(getMultiPlayerData)

# Run Loop

def startProgram():
    try:
        basic.clear_screen()
        led.plot_brightness(OtherX, OtherY, (255 / 2))
        led.plot(PlayerX, PlayerY)
    except:
        basic.show_string("Error On Startup")

basic.forever(startProgram)
