from .functions import *

def check_value(value):
    """
    Check if a value is numeric
    """

    try:
        value / 2
    except:
        raise Exception('The value need be numeric')

class Point():#Just a 2D point, A(x, y)
    """
    This class simulates 2D points, type A(x, y)

    There are two atributes:
    - x: is a float or integer number, this is the first coordinate for points
    - y: is a float or integer number, this is the second coordinate for points
    """
    def __init__(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y

    def get_x(self):
        """
        Return the x value
        """
        return self.x

    def get_y(self):
        """
        Return the y value
        """
        return self.y

    def set_x(self, new_x):
        """
        Set the value of x for a new numeric value
        """
        check_value(new_x)
        self.x = new_x

    def set_y(self, new_y):
        """
        Set the value of y for a new numeric value
        """
        check_value(new_y)
        self.y = new_y

    def is_in_func(self, function):
        """
        Parameters
        __________
        function: is an object from Function class in the archive functions.py
        
        Return True if the point is in function, a point is created using the self
        value of x in the function, so if the y value of this new point is the same
        of the self point. then these points are the same and return True. else return
        False
        """
        tester = function.get_point(self.get_x())
        if tester.get_y() == self.get_y():
            return True
        else:
            return False

    def get_location(self):
        """
        Only a visual way to see the coordinates
        """
        return f'x={self.get_x()}, y={self.get_y()}'

    def get_location_array(self):
        """
        Get the coordinates in a list
        """
        loc = [self.get_x(), self.get_y()]
        return loc

def distance_points(point1, point2):
    """
    return a float number, that show the distance between two point in a cartesian plan
    using the Pythagorean theorem
    """
    delta_x = abs(point1.get_x() - point2.get_x())
    delta_y = abs(point1.get_y() - point2.get_y())
    dist = (delta_x ** 2 + delta_y ** 2) ** (1/2)
    return dist
