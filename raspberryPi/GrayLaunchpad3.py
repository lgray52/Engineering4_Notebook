# type: ignore

from time import sleep
import board
import digitalio

ledGreen = digitalio.DigitalInOut(board.GP15)  # set up green led, connnect to bottom left pin
ledGreen.direction = digitalio.Direction.OUTPUT

ledRed = digitalio.DigitalInOut(board.GP16)  # set up red led, connect to bottom right pin
ledRed.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.GP0)
button.pull = digitalio.Pull.UP  # set up button to be True when NOT pressed

while True:
  if button.value == False:  # if button is pressed
    for i in range(10, 0, -1):  # loop from 10-1, backwards by 1
        # if button.value == False:
        #     print("ABORT LAUNCH")
        #     while button.value == True:
        #         pass

        print(i)  # print out count
        ledRed.value = True  # blink on
        sleep(.5)  # one second between each count
        ledRed.value = False
        sleep(.5)  # blink off
    print("LIFTOFF") # once it counts down to 0, print liftoff

    while True:
        ledGreen.value = True  # keep the green light on