# type: ignore

import adafruit_mpu6050 as imu
import busio
import board
from time import sleep
import digitalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio

displayio.release_displays()

sdaPin = board.GP2  # define which SDA & SCL pins to use - HAVE TO BE CONNECTED TO SAME I2C ON PICO
sclPin = board.GP3
i2c = busio.I2C(sclPin, sdaPin)

mpu = imu.MPU6050(i2c, address = 0x68)  # set up mpu sensor accelerometer - device address from test code

led = digitalio.DigitalInOut(board.GP15)  # connect led to board
led.direction = digitalio.Direction.OUTPUT

display_bus = displayio.I2CDisplay(i2c, device_address = 0x3d, reset = board.GP5)  # set up oled screen - device address from test code
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

# in order to pull a fancy list (called a tuple) of the x, y, and z acceleration value in m/s^2, would call mpu.acceleration
# for angular velocity, would call mpu.gyro

while True:
    accelerationVals = mpu.acceleration
    angularVals = mpu.gyro

    splash = displayio.Group()

    title = f"Angular Velocities:"
    line1 = f"x velocty: {round(angularVals[0], 3)}"  # make lines to print with x, y, and z angular velocities rounded to 3 decimals
    line2 = f"y velocity: {round(angularVals[1], 3)}"
    line3 = f"z velocity: {round(angularVals[2], 3)}"

    titleLine = label.Label(terminalio.FONT, text = title, color = 0xFFFF00, x = 5, y = 5)  # print to screen, and tell it where (coordinate) to start the text
    splash.append(titleLine)  # add this line to splash

    firstLine = label.Label(terminalio.FONT, text = line1, color = 0xFFFF00, x = 5, y = 15)  # x-coordinate the same, changed the y-coordinate to lower on screen
    splash.append(firstLine)

    secondLine = label.Label(terminalio.FONT, text = line2, color = 0xFFFF00, x = 5, y = 25)
    splash.append(secondLine)

    thirdLine = label.Label(terminalio.FONT, text = line3, color = 0xFFFF00, x = 5, y = 35)
    splash.append(thirdLine)

    display.show(splash)

    print(f"X acceleration: {accelerationVals[0]} m/s2")
    print(f"Y acceleration: {accelerationVals[1]} m/s2")
    print(f"Z acceleration: {accelerationVals[2]} m/s2")
    print("")
    sleep(.25)

    if accelerationVals[2] <= 1:
        led.value = True
        print("WARNING")
    
    else:
        led.value = False