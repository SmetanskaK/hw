import math


def cone_square_and_volume(radius, height):
    square_of_cone = math.pi * radius * (radius + math.sqrt(radius ** 2 + height ** 2))
    volume_of_cone = 1 / 3 * math.pi * (radius ** 2) * height
    return square_of_cone, volume_of_cone


result_1, result_2 = cone_square_and_volume(9, 6.7)
print("Square of cone is %.2f, volume of cone is %.2f" % (result_1, result_2))
