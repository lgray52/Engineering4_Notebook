# type: ignore

from time import sleep
import circuitpython-schedule as schedule
from adafruit_datetime import datetime
import pwmio
import board

servoSetup = pwmio.PWMOut(board.GP28, duty_cycle = 2 ** 15, frequency = 50)  # servo set up
myServo = servo.Servo(servoSetup, min_pulse = 500, max_pulse = 2500)

myServo.angle = 0

def servoMove():
    myServo.angle = 180
    sleep(10)
    myServo.angle = 0

schedule.every(24).hours.until(datetime()).do(servoMove)

while True:
    schedule.run_pending()

# Schedule library CP: https://circuitpython-schedule.readthedocs.io/en/latest/