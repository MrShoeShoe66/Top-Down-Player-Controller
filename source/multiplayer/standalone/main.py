import microbit as system

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
system.input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    toggleInputType()
system.input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    MovePlayerY()
    sendUserData()
system.input.on_button_pressed(Button.B, on_button_pressed_b)

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

system.radio.set_transmit_power(5)
system.radio.set_group(194)

def verifiyConection():
    system.radio.send_value("ping", 0)

verifiyConection()

def sendUserData():
    system.radio.send_value("x", PlayerX)
    system.radio.send_value("y", PlayerY)

def getMultiPlayerData(name, value):
    global OtherX, OtherY
    if name == "x":
        OtherX = value
    elif name == "y":
        OtherY = value
    elif name == "ping":
        sendUserData()

system.radio.on_received_value(getMultiPlayerData)

# Run Loop

def startProgram():
    try:
        system.basic.clear_screen()
        system.led.plot_brightness(OtherX, OtherY, (255 / 2))
        system.led.plot(PlayerX, PlayerY)
    except:
        system.basic.show_string("Error On Startup")

system.basic.forever(startProgram)
