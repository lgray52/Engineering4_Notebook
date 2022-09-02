# type: ignore

import board
import digitalio
from time import sleep

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    sleep(1)
    led.value = False
    sleep(1)