//  Move Player Left/Right

function MovePlayerX() {
    
    if (inputToggleVar) {
        if (PlayerX == 4) {
            
        } else {
            PlayerX = PlayerX + 1
        }
        
    } else if (PlayerX == 0) {
        
    } else {
        PlayerX = PlayerX - 1
    }
    
}

//  Move Player Up/Down

function MovePlayerY() {
    
    if (inputToggleVar) {
        if (PlayerY == 4) {
            
        } else {
            PlayerY = PlayerY + 1
        }
        
    } else if (PlayerY == 0) {
        
    } else {
        PlayerY = PlayerY - 1
    }
    
}

//  Call Move CMD

function a_button() {
    MovePlayerX()
}
input.onButtonPressed(Button.A, a_button)

function ab_buttton() {
    toggleInputType()
}
input.onButtonPressed(Button.AB, ab_buttton)

function b_button() {
    MovePlayerY()
}
input.onButtonPressed(Button.B, b_button)

//  Toggle Direction
function toggleInputType() {
    
    inputToggleVar = !inputToggleVar
}

//  Set varyables
PlayerX = 2
PlayerY = 2
inputToggleVar = true

//  Start Program

function programLoop() {
    basic.clearScreen()
    led.plot(PlayerX, PlayerY)
}
basic.programLoop()
