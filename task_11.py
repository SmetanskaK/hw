import math


def degrees2radians(degrees):
    radians = (degrees * math.pi) / 180
    return radians


radians_1 = degrees2radians(40)
cos = math.cos(radians_1)
print("Result is %.2f" % cos)

radians_2 = degrees2radians(45)
cos = math.cos(radians_2)
print("Result is %.2f" % cos)

radians_3 = degrees2radians(60)
cos = math.cos(radians_3)
print("Result is %.2f" % cos)
