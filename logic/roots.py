# this is a python file
import cmath
import math

def root (a,b,c):
    d = ((b**2)-(4*a*c))
    d = int(d)
    if int(d) >= 0 :
        d1 = math.sqrt((b**2)-(4*a*c))
        root_1 = (-b - d1)/(2*a)
        root_2 = (-b + d1)/(2*a)
        return (root_1, root_2)
    else:
        print("The Determinant is Negative Real Roots Don't Exist")
        d2 = cmath.sqrt((b**2)-(4*a*c))
        root_1 = (-b - d2)/(2*a)
        root_2 = (-b + d2)/(2*a)
        return (root_1, root_2)
