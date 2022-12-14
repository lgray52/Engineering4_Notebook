import numpy as np

def enterCoordinates():
    while True:
        print("Please enter vertices in 'x1, y1, x2, y2, x3, y3' form")
        x1, y1, x2, y2, x3, y3 = input().split(',')  # split the string on every comma
        print("Calculating area ...")

        try:
            return float(x1), float(y1), float(x2), float(y2), float(x3), float(y3)  # convert each coordinate to a float
        except:  # if the "try" throws an error, do this instead
            print("Incorrect input format. Please try again.")  # if the coordinates entered aren't numbers, they can't be converted into floats, and the try will not complete


def findArea(x1, y1, x2, y2, x3, y3):  # takes all of the coordinates
    array = np.array([[x1, y1, 1],  # use matrix to get determinant for area
                      [x2, y2, 1],
                      [x3, y3, 1]])
    area = (1/2)*abs(np.linalg.det(array))  # 1/2 the absolute val of the determinant of the matrix = the area of triangle
    
    return area