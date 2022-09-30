from grayLandingLib import enterCoordinates, findArea

while True:
    x1, y1, x2, y2, x3, y3 = enterCoordinates()
    area = findArea(x1, y1, x2, y2, x3, y3)

    print(f"The area of triangle with vertices at ({x1}, {y1}), ({x2}, {y2}), and ({x3}, {y3}) kilometers is {area} square kilometers")