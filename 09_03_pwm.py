#09_03_pwm.py

import gpiozero

led = gpiozero.PWMLED(18)

while True:
    duty_s = input("Enter Brightness (0 to 100):")
    duty = float(duty_s) / 100.0
    led.value = duty