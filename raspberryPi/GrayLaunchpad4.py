# type: ignore

from time import sleep
import board
import digitalio
import pwmio
from adafruit_motor import servo

ledGreen = digitalio.DigitalInOut(board.GP15)  # set up green led, connnect to bottom left pin
ledGreen.direction = digitalio.Direction.OUTPUT

ledRed = digitalio.DigitalInOut(board.GP16)  # set up red led, connect to bottom right pin
ledRed.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.GP0)
button.pull = digitalio.Pull.UP  # set up button to be True when NOT pressed

servoSetup = pwmio.PWMOut(board.GP28, duty_cycle = 2 ** 15, frequency = 50)  # servo set up
myServo = servo.Servo(servoSetup, min_pulse = 500, max_pulse = 2500)

angle = 0  # set up variable for angle
myServo.angle = angle

while True:
  if button.value == False:  # if button is pressed
    for i in range(10, 3, -1):  # loop from 10-4, backwards by 1
        print(i)  # print out count
        ledRed.value = True  # blink on
        sleep(.5)  # one second between each count
        ledRed.value = False
        sleep(.5)  # blink off

    for i in range(3, 0, -1):  # starting at t = -3s, in order to turn servo @ correct time
      print(i)
      ledRed.value = True
      angle_stop = angle + 30  # set stop point 30 degrees ahead of where angle is
      for x in range(angle, angle_stop, 6):  # sweep servo for .5 seconds
        myServo.angle = x
        sleep(.1)
      angle = angle_stop  # set current angle to where is stopped
      ledRed.value = False
      angle_stop = angle + 30  # set new stop for an additional 30 degrees
      for x in range(angle, angle_stop, 6):  # sweep servo for the remaining .5 seconds
        myServo.angle = x
        sleep(.1)
      angle = angle_stop  # and set angle to where it currently is again
    
    print("LIFTOFF") # once it counts down to 0, print liftoff
    myServo.angle = 180

    while True:
        ledGreen.value = True  # keep the green light on