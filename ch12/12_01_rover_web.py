# 12_01_rover_web.py

from bottle import route, run, template, request
from motor_driver_i2c import MotorDriver

motors = MotorDriver()

# Handler for the home page
@route('/')
def index():
    cmd = request.GET.get('command', '')
    if cmd == 'f':
        motors.forward()
    elif cmd == 'l':
        motors.left(0, 0.5) # turn at half speed
    elif cmd == 's':
        motors.stop()
    elif cmd == 'r':
        motors.right(0, 0.5)
    elif cmd == 'b':
        motors.reverse(0, 0.3) # reverse slowly
    return template('home.tpl')
        
run(host="0.0.0.0", port=80)
