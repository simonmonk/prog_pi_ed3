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
        pwm.setDutycycle(self.PWMA, left_pwm)
        if left_dir == 1:
            pwm.setLevel(self.AIN1, 0)
            pwm.setLevel(self.AIN2, 1)
        else:
            pwm.setLevel(self.AIN1, 1)
            pwm.setLevel(self.AIN2, 0)
        pwm.setDutycycle(self.PWMB, right_pwm)
        if right_dir == 1:
            pwm.setLevel(self.BIN1, 0)
            pwm.setLevel(self.BIN2, 1)
        else:
            pwm.setLevel(self.BIN1, 1)
            pwm.setLevel(self.BIN2, 0)


m = MotorDriver()
m.set_motors(50, 1, 25, 0)
input("stop")
m.set_motors(0, 0, 0, 0)