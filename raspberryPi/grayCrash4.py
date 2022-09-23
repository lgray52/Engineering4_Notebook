# type: ignore

from imp import init_builtin
import adafruit_mpu6050 as imu
import busio
import board
from time import sleep
import digitalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
from terminalio import FONT
import displayio
import adafruit_mpl3115a2

displayio.release_displays()

sdaPin = board.GP2  # define which SDA & SCL pins to use - HAVE TO BE CONNECTED TO SAME I2C ON PICO
sclPin = board.GP3
i2c = busio.I2C(sclPin, sdaPin)

mpu = imu.MPU6050(i2c, address = 0x68)  # set up mpu sensor accelerometer - device address from test code

led = digitalio.DigitalInOut(board.GP15)  # connect led to board
led.direction = digitalio.Direction.OUTPUT

display_bus = displayio.I2CDisplay(i2c, device_address = 0x3d, reset = board.GP5)  # set up oled screen - device address from test code
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

altimeter = adafruit_mpl3115a2.MPL3115A2(i2c, address = 0x60)  # set up altimeter

# in order to pull a fancy list (called a tuple) of the x, y, and z acceleration value in m/s^2, would call mpu.acceleration
# for angular velocity, would call mpu.gyro

groundLevel = altimeter.altitude  # alimeter measures from sea level - set intial val of ground level

while True:
    accelerationVals = mpu.acceleration
    angularVals = mpu.gyro
    alt = altimeter.altitude  # pull the current altitude

    splash = displayio.Group()  # set up "splash" for display screen

    title = f"Angular Velocities:"
    line1 = f"x velocty: {round(angularVals[0], 3)}"  # make lines to print with x, y, and z angular velocities rounded to 3 decimals
    line2 = f"y velocity: {round(angularVals[1], 3)}"
    line3 = f"z velocity: {round(angularVals[2], 3)}"

    titleLine = label.Label(FONT, text = title, color = 0xFFFF00, x = 5, y = 5)  # format title line; set text to start at screen coordinate (5,5)
    splash.append(titleLine)  # add title to what the screen is showing

    firstLine = label.Label(FONT, text = line1, color = 0xFFFF00, x = 5, y = 15)  # set text a little lower on the screen - same x to start line in same place
    splash.append(firstLine)

    secondLine = label.Label(FONT, text = line2, color = 0xFFFF00, x = 5, y = 25)
    splash.append(secondLine)

    thirdLine = label.Label(FONT, text = line3, color = 0xFFFF00, x = 5, y = 35)
    splash.append(thirdLine)

    display.show(splash)  # print to screen

    print(f"X acceleration: {accelerationVals[0]} m/s2")
    print(f"Y acceleration: {accelerationVals[1]} m/s2")
    print(f"Z acceleration: {accelerationVals[2]} m/s2")
    print("")
    sleep(.25)

    if accelerationVals[2] <= 1 and alt - groundLevel <= 3:  # add condition that light is only on if altitude is less than 3 meters
        led.value = True
        print("WARNING")
        print(alt - groundLevel)  # altitude minus the ground level in order to get height above the ground
    
    else:
        led.value = False