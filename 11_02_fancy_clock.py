# 11_02_fancy_clock.py

import board, time, gpiozero
from adafruit_ht16k33.segments import Seg7x4
from datetime import datetime

switch = gpiozero.Button(23, pull_up=True)
i2c = board.I2C()
display = Seg7x4(i2c)
display.brightness = 0.3
show_colon = True
time_mode, seconds_mode, date_mode = range(3)
disp_mode = time_mode

def display_time():
    global show_colon
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

def display_seconds():
    now = datetime.now()
    current_seconds = now.strftime("  %S")
    display.print(current_seconds)
    time.sleep(0.5)

def display_date():
    now = datetime.now()
    current_date = now.strftime("%m%d")
    display.print(current_date)
    time.sleep(0.5)

while True:
    if switch.is_pressed:
        disp_mode = disp_mode + 1
        if disp_mode > date_mode:
            disp_mode = time_mode
    if disp_mode == time_mode:
        display_time()
    elif disp_mode == seconds_mode:
        display_seconds()
    elif disp_mode == date_mode:
        display_date()