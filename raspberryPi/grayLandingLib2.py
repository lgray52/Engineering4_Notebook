# import numpy as np

def enterCoordinates():
    while True:
        print("Please enter vertices in 'x1, y1, x2, y2, x3, y3' form")
        x1, y1, x2, y2, x3, y3 = input().split(',')  # split the string on every comma
        print("Calculating area ...")

        try:
            return float(x1), float(y1), float(x2), float(y2), float(x3), float(y3)  # convert each coordinate to a float
        except:  # if the "try" throws an error, do this instead
            print("Incorrect input format. Please try again.")  # if the coordinates entered aren't numbers, they can't be converted into floats, and the try will not complete


def findAreaPico(x1, y1, x2, y2, x3, y3):
    area = (1/2)*abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))

    return area