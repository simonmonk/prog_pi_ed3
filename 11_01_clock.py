# 11_01_clock.py

import board, time
from adafruit_ht16k33.segments import Seg7x4
from datetime import datetime

i2c = board.I2C()
display = Seg7x4(i2c)
display.brightness = 0.3
show_colon = True

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    display.print(current_time)
    if show_colon:
        display.colon = True
        show_colon = False
    else:
        display.colon = False
        show_colon = True
    time.sleep(0.5)