# Engineering4_Notebook


## TableOfContents
* [Launchpad Code 1](#Launchpad1)
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
![blink countdown]([link to github page for gif](https://github.com/lgray52/Engineering4_Notebook/blob/main/images/launchpad2_evidence.gif))

### Wiring
<img src="images/launchpad2_wiring.png" alt="pico with two leds" height="300">

### Reflection
This assignment was a good introduction to infinite "while True" loops, which loop code continuously until it is turned off. It also serves a good intro to connecting LEDs as outputs and the syntax with digitalio required with that. Also, it's very neat that the Pico has 8 grounds (though it's seems a little excessive).

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
