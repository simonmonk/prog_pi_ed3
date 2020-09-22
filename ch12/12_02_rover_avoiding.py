# 12_02_rover_avoiding.py
from gpiozero import DistanceSensor
from motor_driver_i2c import MotorDriver
import time, random

motors = MotorDriver()
rangefinder = DistanceSensor(echo=18, trigger=17)

def turn_randomly():
    turn_time = random.randint(1, 3)
    if random.randint(1, 2) == 1:
        motors.left(turn_time) 
    else:
        motors.right(turn_time)
    motors.stop()

while True:
    distance = rangefinder.distance * 100 # convert to cm
    print(distance)
    if distance < 20:
        motors.stop()
    elif distance < 50:
        turn_randomly()
    else:
        motors.forward()
    time.sleep(0.2)
