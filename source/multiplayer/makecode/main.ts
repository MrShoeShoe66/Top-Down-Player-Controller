//  Move Player Left/Right
function MovePlayerX() {
    
    if (inputToggleVar) {
        if (!(PlayerX == 4)) {
            PlayerX = PlayerX + 1
        }
        
    } else if (!(PlayerX == 0)) {
        PlayerX = PlayerX - 1
    }
    
}

//  Move Player Up/Down
function MovePlayerY() {
    
    if (inputToggleVar) {
        if (!(PlayerY == 4)) {
            PlayerY = PlayerY + 1
        }
        
    } else if (!(PlayerY == 0)) {
        PlayerY = PlayerY - 1
    }
    
}

//  Call Move CMD
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    MovePlayerX()
    sendUserData()
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    toggleInputType()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    MovePlayerY()
    sendUserData()
})
//  Toggle Direction
function toggleInputType() {
    
    inputToggleVar = !inputToggleVar
}

//  Set varyables
let PlayerX = 2
let PlayerY = 2
let inputToggleVar = true
let OtherX = 2
let OtherY = 2

//  Start MultiPlayer
radio.setTransmitPower(5)
radio.setGroup(194)
function verifiyConection() {
    radio.sendValue("ping", 0)
}

verifiyConection()
function sendUserData() {
    radio.sendValue("x", PlayerX)
    radio.sendValue("y", PlayerY)
}

radio.onReceivedValue(function getMultiPlayerData(name: string, value: number) {
    
    if (name == "x") {
        OtherX = value
    } else if (name == "y") {
        OtherY = value
    } else if (name == "ping") {
        sendUserData()
    }
    
})

//  Run Loop
basic.forever(function startProgram() {
    try {
        basic.clearScreen()
        led.plotBrightness(OtherX, OtherY, 255 / 2)
        led.plot(PlayerX, PlayerY)
    }
    catch (_) {
        basic.showString("Error On Startup")
    }
    
})
