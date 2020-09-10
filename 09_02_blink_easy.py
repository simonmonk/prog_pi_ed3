#09_02_blink_easy.py

import gpiozero, time

led = gpiozero.LED(18)

led.blink(on_time=0.5, off_time=0.5)