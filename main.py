# Import the Bluetooth Low Energy API module
import bluetooth, microbit


# Event handler for Bluetooth connection

def on_bluetooth_connected():

    # Add actions to perform when Bluetooth is connected

    pass



# Register the event handler

bluetooth.on_bluetooth_connected(on_bluetooth_connected)



# Event handler for Bluetooth disconnection

def on_bluetooth_disconnected():

    # Add actions to perform when Bluetooth is disconnected

    pass



# Register the event handler

bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)



# Initialize variables

now = 0

advertise = False

now1 = 0

Xold = 0

Yold = 0

movement = False

Zold = 0

Ymovement = 0

Xmovement = 0

Zmovement = 0

timet = 12 * 60 * 1000 # Time threshold in milliseconds to start advertising if no movement detected

Zthreshold = 300  # Threshold for Z-axis movement detection

Ythreshold = 300  # Threshold for Y-axis movement detection

Xthreshold = 300  # Threshold for X-axis movement detection



# Stop any ongoing advertising

bluetooth.stop_advertising()



def on_movement():
    hardwario.on_movement(on_movement)

    

# Main loop to check for movement and control Bluetooth advertising

def on_forever():

    global Zmovement, Xmovement, Ymovement, Zold, movement, Yold, Xold, now1, advertise, now

    

    # Read accelerometer values for all three dimensions
    Zmovement = microbit.accelerometer.get_z()

    Xmovement = microbit.accelerometer.get_x()

    Ymovement = microbit.accelerometer.get_y()

    # Check if there's significant movement in the Z-axis compared to previous reading
    if abs(Zmovement - Zold) > Zthreshold:

        Zold = Zmovement

        movement = True

        # Display a visual indicator of movement on the LED matrix (Z-axis)
        basic.show_leds("""

            # . . . .

            . . . . .

            . . . . .

            . . . . .

            . . . . .

            """)

    

    # Check if there's significant movement in the Y-axis compared to previous reading

    if abs(Ymovement - Yold) > Ythreshold:

        Yold = Ymovement

        movement = True

        # Display a visual indicator of movement on the LED matrix (Y-axis)

        basic.show_leds("""

            . # . . .

            . . . . .

            . . . . .

            . . . . .

            . . . . .

            """)

    

    # Check if there's significant movement in the X-axis compared to previous reading

    if abs(Xmovement - Xold) > Xthreshold:

        Xold = Xmovement

        movement = True

        # Display a visual indicator of movement on the LED matrix (X-axis)

        basic.show_leds("""

            . . # . .

            . . . . .

            . . . . .

            . . . . .

            . . . . .

            """)

    

    # If movement was detected, reset the timer and stop advertising

    if movement:

        movement = False

        now1 = input.running_time()

        advertise = False

        bluetooth.stop_advertising()

        basic.pause(500)

        basic.clear_screen()

    

    # If no movement detected for the set time threshold, start advertising over Bluetooth

    else:

        now = input.running_time()

        if now > now1 + timet * 1000 * 60:

            if not advertise:

                # Display a visual indicator that advertising is starting on the LED matrix

                basic.show_leds("""

                    . . . . .

                    . . . . .

                    . . # . .

                    . . . . .

                    . . . . .

                    """)

                bluetooth.advertise_url("http://www.google.com", 7, False)

                advertise = True



# Run the main loop forever

basic.forever(on_forever)