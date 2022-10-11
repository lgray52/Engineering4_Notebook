# type: ignore

from grayLandingLib3 import areaDistance, coordinateSeparator
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

from time import sleep

sdaPin = board.GP2  # define which SDA & SCL pins to use
sclPin = board.GP3
i2c = busio.I2C(sclPin, sdaPin)

display_bus = displayio.I2CDisplay(i2c, device_address = 0x3d, reset = board.GP5)  # set up oled screen - device address from test code
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

points = [['-50, -17, -57, 12, -22, -7'],['28, -14, 60, -7, 54, 18'],['45, 30, 51, -1, 18, 6'],['5, 5, 19, 15, 22, 10']]
# points = [['-2, -30, -19, -8, -44, -18'],['7, -14, 60, -7, 33, -6'],['5,5,-8,9,0,-6'],['63,30,60,19,29,16']]

triangleVals = []  # make a blank list to store area and centroids of triangles

for i in range(len(points)):
    print(points[i])
    x1, y1, x2, y2, x3, y3 = coordinateSeparator(points[i])  # separate the coordinates from each section of the list
    vals = areaDistance(x1, y1, x2, y2, x3, y3)  # find the values from those vertices
    triangleVals.append(vals)  # add the area and centroids of each triangle
    print(vals)
    area = vals[0]  # relevant area
    centroid = vals[1]

    splash = displayio.Group()  # make display group

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

    sleep(2)

print(triangleVals)

badTriangles = []
for i in range(len(triangleVals)):  # delete triangles with area less than 100 square km
    if triangleVals[i][0] <= 100:
        badTriangles.append(i)  # save a list of the indexes of the bad triangles

for i in range(len(badTriangles)):
    del triangleVals[badTriangles[i]]  # delete the bad triangles from the lists of triangle vals and the original triangle points list
    del points[badTriangles[i]]

print(points)

centroids = []  # blank list for centroid distances
for i in range(len(triangleVals)):
    centroids.append(triangleVals[i][1])  # add the centroid distances to list
    
closest = min(centroids)  # find the minimum centroid distance
closestIndex = centroids.index(closest)  # find its index in the list, which corresponds to its index in the list of points

x1, y1, x2, y2, x3, y3 = coordinateSeparator(points[closestIndex])  # use the index found to get the points from the points list
areaPlusCentroid = areaDistance(x1, y1, x2, y2, x3, y3)  # get the distance and centroid

txt = f"Closest Area: {round(areaPlusCentroid[0], 2)} \n km2 \n Centroid: {round(areaPlusCentroid[1], 2)} km \n away from base."
print(f"The closest suitable landing area has vertices ({x1}, {y1}), ({x2}, {y2}), and ({x3}, {y3}). The area is {areaPlusCentroid[0]} km2 and the centroid is {areaPlusCentroid[1]} km away from base.")

splash = displayio.Group()  # make display group

showText = label.Label(terminalio.FONT, text = txt, color = 0xFFFF00, x = 5, y = 5)
splash.append(showText)

while True:
    display.show(splash)