import math


def find_quadrant1_lattice_points_of_ellipse(n, a, b):
    """Steps down an ellipse, generating rounded-off coordinates, 
    then checks them.  Returns a list of lattice points, if there
    are any."""
    
    lattice_points = []
    x_intercept = math.sqrt(n/a)
    for x in range(1, math.floor(x_intercept) + 1):
        y = round(math.sqrt((n - a*x**2)/b))
        if y != 0 and n == a*x**2 + b*y**2:
            lattice_points.append((x, y))
            
    return lattice_points


def find_quadrant1_lattice_points_of_hyperbola(n, a, b):
    """Steps up a hyperbola, generating rounded-off coordinates,
    then checks them.  Returns a list of lattice points satisfying
    x > y, if there are any"""
    
    lattice_points = []
    stopping_y = math.sqrt(n/(a+b))
    for y in range(1, math.floor(stopping_y) + 1):
        x = round(math.sqrt((n - b*y**2)/a))
        if x > y and n == a*x**2 + b*y**2:
            lattice_points.append((x, y))
            
    return lattice_points