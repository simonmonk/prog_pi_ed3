# 10_01_RGB_LED.py

from gpiozero import RGBLED
from guizero import App, Slider, Text
from colorzero import Color

rgb_led = RGBLED(18, 23, 24)

red = 0
green = 0
blue = 0

def red_changed(value):
    global red
    red = int(value)
    rgb_led.color = Color(red, green, blue)

def green_changed(value):
    global green
    green = int(value)
    rgb_led.color = Color(red, green, blue)

def blue_changed(value):
    global blue
    blue = int(value)
    rgb_led.color = Color(red, green, blue)

app = App(title='RGB LED', width=500, height=400, layout='grid')

Text(app, text='Red', grid=[0,0]).text_size = 30
Slider(app, command=red_changed, end=255, width=350, height=50, grid=[1,0]).text_size = 30
Text(app, text='Green', grid=[0,1]).text_size = 30
Slider(app, command=green_changed, end=255, width=350, height=50, grid=[1,1]).text_size = 30
Text(app, text='Blue', grid=[0,2]).text_size = 30
Slider(app, command=blue_changed, end=255, width=350, height=50, grid=[1,2]).text_size = 30

app.display()