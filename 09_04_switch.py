#09_04_switch.py

import gpiozero, time

switch = gpiozero.Button(23, pull_up=True)

while True:
    if switch.is_pressed:
        print("Button Pressed")
        time.sleep(0.2)