from pymata4 import pymata4
import time 

board = pymata4.Pymata4(com_port="COM5")  # Specify COM5 as the port

analog_pin = 0
digital_pin = 8

board.set_pin_mode_analog_input(analog_pin)
board.set_pin_mode_digital_input(digital_pin)

while True:
    value, _ = board.analog_read(analog_pin)  # Read analog value and ignore timestamp
    if value is not None:  # Check if the value is valid (not None)
        if value < 1000:
            print("Wet",value)
        else:
            print("Dry",value)
    else:
        print(0)  # Print 0 if the sensor reading is not valid
    time.sleep(1)
