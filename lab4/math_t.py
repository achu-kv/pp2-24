import math

# task 1
def deg_to_rad(deg):
    return math.radians(deg)

# task 2
def area_of_trap(h, b1, b2):
    return (b1 + b2) * h / 2

# task 3
def area_of_poly(n, a):
    area = n * (a ** 2) / (4 * math.tan(math.radians(180 / n)))
    area = round(area, 4)
    if area % 1 == 0:
        return int(area)
    return area

# task 4
def area_of_paral(l, h):
    return l * h

