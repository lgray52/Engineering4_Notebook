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

led = digitalio.DigitalInOut(board.GP15)  # connect led to board
led.direction = digitalio.Direction.OUTPUT

# in order to pull a fancy list (called a tuple) of the x, y, and z acceleration value in m/s^2, would call mpu.acceleration
# for angular velocity, would call mpu.gyro

while True:
    accelerationVals = mpu.acceleration  # give the tuple of the x, y, and z vals a name

    print(f"X acceleration: {accelerationVals[0]} m/s2")  # take x value, value one, out of tuple and print
    print(f"Y acceleration: {accelerationVals[1]} m/s2")
    print(f"Z acceleration: {accelerationVals[2]} m/s2")
    print("")
    sleep(.25)

    # ordinarily, the z acceleration will be around 9.8 m/s2 bc of acceleration due to gravity
    if accelerationVals[2] <= 1:  # if the mpu is on its side, the z acceleration will be close to zero
        led.value = True  # turn the led on
        print("WARNING")
    
    else:
        led.value = False  # otherwise, turn it off - needs to be in an else so it isn't turning on and off every time the loop runs