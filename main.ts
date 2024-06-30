//  Import the Bluetooth Low Energy API module
//  Event handler for Bluetooth connection
//  Register the event handler
bluetooth.onBluetoothConnected(function on_bluetooth_connected() {
    //  Add actions to perform when Bluetooth is connected
    
})
//  Event handler for Bluetooth disconnection
//  Register the event handler
bluetooth.onBluetoothDisconnected(function on_bluetooth_disconnected() {
    //  Add actions to perform when Bluetooth is disconnected
    
})
//  Initialize variables
let now = 0
let advertise = false
let now1 = 0
let Xold = 0
let Yold = 0
let movement = false
let Zold = 0
let Ymovement = 0
let Xmovement = 0
let Zmovement = 0
let timet = 12 * 60 * 1000
//  Time threshold in milliseconds to start advertising if no movement detected
let Zthreshold = 300
//  Threshold for Z-axis movement detection
let Ythreshold = 300
//  Threshold for Y-axis movement detection
let Xthreshold = 300
//  Threshold for X-axis movement detection
//  Stop any ongoing advertising
bluetooth.stopAdvertising()
//  Main loop to check for movement and control Bluetooth advertising
//  Run the main loop forever
basic.forever(function on_forever() {
    
    //  Read accelerometer values for all three dimensions
    Zmovement = input.acceleration(Dimension.Z)
    Xmovement = input.acceleration(Dimension.X)
    Ymovement = input.acceleration(Dimension.Y)
    //  Check if there's significant movement in the Z-axis compared to previous reading
    if (Math.abs(Zmovement - Zold) > Zthreshold) {
        Zold = Zmovement
        movement = true
        //  Display a visual indicator of movement on the LED matrix (Z-axis)
        basic.showLeds(`
            # . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    }
    
    //  Check if there's significant movement in the Y-axis compared to previous reading
    if (Math.abs(Ymovement - Yold) > Ythreshold) {
        Yold = Ymovement
        movement = true
        //  Display a visual indicator of movement on the LED matrix (Y-axis)
        basic.showLeds(`
            . # . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    }
    
    //  Check if there's significant movement in the X-axis compared to previous reading
    if (Math.abs(Xmovement - Xold) > Xthreshold) {
        Xold = Xmovement
        movement = true
        //  Display a visual indicator of movement on the LED matrix (X-axis)
        basic.showLeds(`
            . . # . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    }
    
    //  If movement was detected, reset the timer and stop advertising
    if (movement) {
        movement = false
        now1 = input.runningTime()
        advertise = false
        bluetooth.stopAdvertising()
        basic.pause(500)
        basic.clearScreen()
    } else {
        //  If no movement detected for the set time threshold, start advertising over Bluetooth
        now = input.runningTime()
        if (now > now1 + timet * 1000 * 60) {
            if (!advertise) {
                //  Display a visual indicator that advertising is starting on the LED matrix
                basic.showLeds(`
                    . . . . .
                    . . . . .
                    . . # . .
                    . . . . .
                    . . . . .
                    `)
                bluetooth.advertiseUrl("http://www.google.com", 7, false)
                advertise = true
            }
            
        }
        
    }
    
})
