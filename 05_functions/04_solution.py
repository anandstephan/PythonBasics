import math

def circle_stat(radius):
    area = math.pi * radius ** 2
    circum = 2 * math.pi*radius
    return round(area),round(circum)

print(circle_stat(4))