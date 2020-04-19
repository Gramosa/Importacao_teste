from .functions import *
from .point import *

def intersection_point(function1, function2):
    """
    this function returns a point from the intersection of two functions,
    they need to have a different "a" value to touch
    """
    a = function1.get_a()
    b = function1.get_b()
    c = function2.get_a()
    d = function2.get_b()
    if a != c:#se "a" for igual a "c", as funções serão paralelas e nunca se tocarão
        x = (d - b)/(a - c)
        if x == int(x):
            x = int(x)
    else:
        raise Exception('this functions will never intersect')
    return function1.get_point(x)

def generate_function(point1, point2):
    """
    This function return a Function objetc from the functions.py
    this function is generated from the line connecting two points, these points cannot
    have the same value of x
    """
    y = point1.get_y()
    z = point2.get_y()
    x = point1.get_x()
    w = point2.get_x()
    if x != w:#se "x" for igual a "w", esses pontos terão o mesmo valor de dominio. E não será possível determinar uma função entre eles
        a = (y - z)/(x - w)
        if z != y:#ja que os dominios são diferentes, se "z" for diferente de "y" descarta-se a possibilidade de função linear, e "b" precisa ser calculado
            b = (a*(y*w - z*x))/(z - y)
        else:#função linear
            raise Exception('The function can\'t be constant, only "afim" functions') #poderia ser "y" ou "w", já que ambos são iguais. ou seja "b" será constante
        return Function(a, b)
    else:
        raise Exception('domain of points can\'t be the same')
