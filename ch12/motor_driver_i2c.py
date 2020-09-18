# Class for motor control of Waveshare Motor pHAT

from PCA9685 import PCA9685
import time

pwm = PCA9685(0x40, debug=False)
pwm.setPWMFreq(50)

class MotorDriver():
    def __init__(self):
        self.PWMA = 0
        self.AIN1 = 1
        self.AIN2 = 2
        self.PWMB = 5
        self.BIN1 = 3
        self.BIN2 = 4

    def set_motors(self, left_pwm, left_dir, right_pwm, right_dir):
        pwm.setDutycycle(self.PWMA, left_pwm * 100)
        if left_dir == 1:
            pwm.setLevel(self.AIN1, 0)
            pwm.setLevel(self.AIN2, 1)
        else:
            pwm.setLevel(self.AIN1, 1)
            pwm.setLevel(self.AIN2, 0)
        pwm.setDutycycle(self.PWMB, right_pwm * 100)
        if right_dir == 1:
            pwm.setLevel(self.BIN1, 0)
            pwm.setLevel(self.BIN2, 1)
        else:
            pwm.setLevel(self.BIN1, 1)
            pwm.setLevel(self.BIN2, 0)

    def forward(self, seconds=0, speed=1.0):
        self.set_motors(speed, 0, speed, 0)
        if seconds > 0:
            time.sleep(seconds)
            self.stop()

    def stop(self):
        self.set_motors(0, 0, 0, 0)

    def reverse(self, seconds=0, speed=1.0):
        self.set_motors(speed, 1, speed, 1)
        if seconds > 0:
            time.sleep(seconds)
            self.stop()

    def left(self, seconds=0, speed=0.5):
        self.set_motors(speed, 0, speed, 1)
        if seconds > 0:
            time.sleep(seconds)
            self.stop()

    def right(self, seconds=0, speed=0.5):
        self.set_motors(speed, 1, speed, 0)
        if seconds > 0:
            time.sleep(seconds)
            self.stop()

# m = MotorDriver()
# m.set_motors(1, 1, 0.25, 0)
# input("stop")
# m.stop()
# input("forward")
# m.forward(3, 0.5)
# input("stop")
# m.stop()
# input("left")
# m.left(5)
# input("stop")
# m.stop()
