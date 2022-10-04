# type: ignore

from grayLandingLib2 import enterCoordinates, findAreaPico
import board
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio
import busio

displayio.release_displays()

from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle

sdaPin = board.GP2  # define which SDA & SCL pins to use
sclPin = board.GP3
i2c = busio.I2C(sclPin, sdaPin)

display_bus = displayio.I2CDisplay(i2c, device_address = 0x3d, reset = board.GP5)  # set up oled screen - device address from test code
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

while True:
    splash = displayio.Group()  # make display group

    x1, y1, x2, y2, x3, y3 = enterCoordinates()
    area = findAreaPico(x1, y1, x2, y2, x3, y3)

    print(f"The area of triangle with vertices at ({x1}, {y1}), ({x2}, {y2}), and ({x3}, {y3}) kilometers is {area} square kilometers")

    areaText = label.Label(terminalio.FONT, text = f"{round(area, 2)} km2", color = 0xFFFF00, x = 5, y = 5)
    splash.append(areaText)

    xAxis = Line(64, 0, 64, 64, color = 0xFFFF00)  # draw the x-axis
    splash.append(xAxis)

    yAxis = Line(0, 32, 128, 32, color = 0xFFFF00)  # draw the y-axis
    splash.append(yAxis)

    origin = Circle(64, 32, 5, outline = 0xFFFF00)  # draw a little circle at the origin/base location
    splash.append(origin)

    # need to manipulate the coordinates so they are in the right place on the screen with respect to the center of the screen, (64, 32)
    triangle = Triangle(int(x1) + 64, 32 - int(y1), int(x2) + 64, 32 - int(y2), int(x3) + 64, 32 - int(y3), outline = 0xFFFF00)
    splash.append(triangle)  # plot the triangle with the given points. need integers because no decimal pixels

    display.show(splash)