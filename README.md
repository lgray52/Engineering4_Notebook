# Engineering4_Notebook


## TableOfContents
* Launchpad assignments
    * [Launchpad Code 1](#Launchpad1)
    * [Launchpad Code 2](#Launchpad2)
    * [Launchpad Code 3](#Launchpad3)
    * [Launchpad Code 4](#Launchpad4)
* [Media Test](#MediaTest)

## Launchpad1

### Description & Code
This assignment had you use the serial monitor to print a launch countdown.
[Link to Code](https://github.com/lgray52/Engineering4_Notebook/blob/main/raspberryPi/GrayLaunchpad1.py)

### Evidence
![countdown from 10 to liftoff in VS Code terminal](https://github.com/lgray52/Engineering4_Notebook/blob/main/images/countdownEvidence.gif)

No wiring involved.

### Reflection
A "for" loop is a helpful tool in completing this assignment. A range function also helps, as it gives the "for" loop a number to use for each instance it runs. For example, a "for" loop with a range function from 1 - 10 
```python 
for i in range(1, 10)
```
would assign the variable given (*i* here) to a "for" loop for each number between 1 and 9. So on the first time through the loop *i* would be 1, on the second it would be 2, etc. It only goes up to 9 because on 9 the loop will have run ten times because it includes the first 1. A "for" loop automatically steps by 1, ie adds 1 each time, but you can change that by adding a third parameter to the range function like so,
``` python
for i in range(1, 10, 2)
```
which would change the step to 2. So for this function, on the first time through the loop *i* would be 1, on the second time *i* would be 3, on the third it would be 5, etc. You can ask go backward, or add negative numbers, like in this assignment where I needed to count by -1 from 10 down to 1. 

[Back to Table of Contents](#Table_of_Contents)


## Launchpad2

### Description & Code
The purpose of this assignment was to turn on LEDs in correspondence with the countdown. In order to complete this, physical LEDs plugged into the Pico on a breadboard were required. 

```python
# type: ignore

from time import sleep
import board
import digitalio

ledGreen = digitalio.DigitalInOut(board.GP15)  # set up green led, connnect to bottom left pin
ledGreen.direction = digitalio.Direction.OUTPUT

ledRed = digitalio.DigitalInOut(board.GP16)  # set up red led, connect to bottom right pin
ledRed.direction = digitalio.Direction.OUTPUT

for i in range(10,0, -1):  # loop from 10-1, backwards by 1
    print(i)  # print out count
    ledRed.value = True  # blink on
    sleep(.5)  # one second between each count
    ledRed.value = False
    sleep(.5)  # blink off
print("LIFTOFF") # once it counts down to 0, print liftoff

while True:
    ledGreen.value = True  # keep the green light on
```
[Link to Code](https://github.com/lgray52/Engineering4_Notebook/blob/main/raspberryPi/GrayLaunchpad2.py)

### Evidence
![blink countdown](https://github.com/lgray52/Engineering4_Notebook/blob/main/images/launchpad2_evidence_better.gif)

### Wiring
<img src="images/launchpad2_wiring.png" alt="pico with two leds" height="300">

### Reflection
This assignment was a good introduction to infinite "while True" loops, which loop code continuously until it is turned off. It also serves a good intro to connecting LEDs as outputs and the syntax with digitalio required with that. Also, it's very neat that the Pico has 8 grounds (though it's seems a little excessive).

[Back to Table of Contents](#Table_of_Contents)


## Launchpad3

### Description & Code
Instead of automatically starting the launch countdown when the code starts running, the purpose of this code was to be able to start the countdown with a button. This required a physical button, but also some understanding of the board and its circuits. 

```python
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
        print(i)  # print out count
        ledRed.value = True  # blink on
        sleep(.5)  # one second between each count
        ledRed.value = False
        sleep(.5)  # blink off
    print("LIFTOFF") # once it counts down to 0, print liftoff

    while True:
        ledGreen.value = True  # keep the green light on
```
[Link to Code](https://github.com/lgray52/Engineering4_Notebook/blob/main/raspberryPi/GrayLaunchpad3.py)

### Evidence, including wiring
![button activated launch countdown](https://github.com/lgray52/Engineering4_Notebook/blob/main/images/launchpad3_evidence.gif)

### Reflection
This assignment introduced buttons, but also the Pico's internal pull up resistors. These are very useful when controlling buttons, as buttons need to be pulled either up or down when they are set up, meaning they either do or don't have complete circuits as their default "off" state. I pulled my button UP, so the circuit is completed when it is in its "off" state, or when it is not pressed. When it is pressed, the circuit is broken and no longer connects to ground, meaning it reads to the board as "False." This is why I use the statement
```python
if button.value == False
```
to check if the button is being pressed. The function is in an infinite "while" loop so it is always checking for the button to be pressed.

[Back to Table of Contents](#Table_of_Contents)


## Launchpad4

### Description & Code
The final assignment in the Launchpad series adds the use of a servo motor. I did the spicy version, which begins to move the servo on t = -3s, and completes moving the servo a full 180 degrees at liftoff. 

```python
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
    for i in range(10, 3, -1):  # loop from 10-1, backwards by 1
        print(i)  # print out count
        ledRed.value = True  # blink on
        sleep(.5)  # one second between each count
        ledRed.value = False
        sleep(.5)  # blink off

    for i in range(3, 0, -1):
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
```
[Link to Code](https://github.com/lgray52/Engineering4_Notebook/blob/main/raspberryPi/GrayLaunchpad4.py)

### Evidence
![button activated countdown with servo](https://github.com/lgray52/Engineering4_Notebook/blob/main/images/launchpad4Evidence.gif)

### Wiring
<img src="images/launchpad4_wiring.PNG" alt="pico with leds, button, and servo" height="300">

### Reflection
I use several "for" loops to add small increments to the angle of the servo and still achieve the correct amount of time between each blink. In order to achieve that though, I repeatedly switched variable values with each other so that when the loop repeated again, the servo wouldn't be sent back to where it started before. This was a good reminder as to how variables take on values, and how to strategically switch them to store the values of important information to be used by the code in the future. For example, I set the variable "angle_stop" to keep the value of where the angle should stop in the loop, and after the end of every loop, I added the number of degrees I wanted it to go to in the next round. However, I stored the previous value of the angle where the servo stopped in my variable for the current angle, "angle." So between each LED blink, I looped something like this:
```python
"""set to correct stop point"""
angle_stop = angle + 30

"""loop for servo turn"""
for x in range(angle, angle_stop, increment):
   myServo.angle = x
   sleep(time)

"""save where the servo stopped as the current angle"""
angle = angle_stop

"""blink LED"""
led.value = # True or False
```

[Back to Table of Contents](#Table_of_Contents)


## MediaTest

### Test Link
[link test](https://www.webhamster.com/)

### Code Link
[code link](https://github.com/lgray52/Engineering4_Notebook/blob/main/raspberryPi/test.py)

### Test Image
<img src="images/stephans_quintet.jpg" alt="NASA Webb telescope image of Stephan's Quintet, five galxies nearby in Earth's sky" height="600">

### Test GIF
<img src="images/hamster_dance.gif" alt="animated hamsters dancing" height="300">

[Back to Table of Contents](#TableOfContents)
