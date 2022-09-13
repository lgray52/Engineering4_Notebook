# type: ignore

import adafruit_mpu6050 as imu
import busio
import board

sdaPin = board.GP2  # define which SDA & SCL pins to use - HAVE TO BE CONNECTED TO SAME I2C ON PICO
sclPin = board.GP3
i2c = busio.I2C(sclPin, sdaPin)

mpu = adafruit_mpu6050.MPU6050(i2c)  # set up mpu sensor accelerometer

# in order to pull a fancy list (called a tuple) of the x, y, and z acceleration value in m/s^2, would call mpu.acceleration
# for angular velocity, would call mpu.gyro

