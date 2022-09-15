# type: ignore

import adafruit_mpu6050 as imu
import busio
import board
from time import sleep
import digitalio

sdaPin = board.GP2  # define which SDA & SCL pins to use - HAVE TO BE CONNECTED TO SAME I2C ON PICO
sclPin = board.GP3
i2c = busio.I2C(sclPin, sdaPin)

mpu = imu.MPU6050(i2c)  # set up mpu sensor accelerometer

led = digitalio.DigitalInOut(board.GP16)  # connect led to board
led.direction = digitalio.Direction.OUTPUT

# in order to pull a fancy list (called a tuple) of the x, y, and z acceleration value in m/s^2, would call mpu.acceleration
# for angular velocity, would call mpu.gyro

while True:
    accelerationVals = mpu.acceleration
    print(f"X acceleration: {accelerationVals[0]} m/s2")
    print(f"Y acceleration: {accelerationVals[1]} m/s2")
    print(f"Z acceleration: {accelerationVals[2]} m/s2")
    print("")
    sleep(.25)

    if accelerationVals[2] <= 1:
        led.value = True