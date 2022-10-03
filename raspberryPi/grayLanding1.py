from grayLandingLib import enterCoordinates, findArea

while True:  # loop so it will ask again
    x1, y1, x2, y2, x3, y3 = enterCoordinates()  # use function to break coordinates into list
    area = findArea(x1, y1, x2, y2, x3, y3)  # use function to find the area of the triangle

    print(f"The area of triangle with vertices at ({x1}, {y1}), ({x2}, {y2}), and ({x3}, {y3}) kilometers is {area} square kilometers")