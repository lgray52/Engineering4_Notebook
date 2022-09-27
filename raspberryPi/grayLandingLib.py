import numpy as np

def findArea(x1, y1, x2, y2, x3, y3):  # takes all of the coordinates
    array = np.array([[x1, y1, 1],  # use matrix to get determinant for area
                      [x2, y2, 1],
                      [x3, y3, 1]])
    area = (1/2)*abs(np.linalg.det(array))  # 1/2 the absolute val of the determinant of the matrix = the area of triangle
    
    return area

